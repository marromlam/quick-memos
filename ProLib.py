# -*- coding: UTF-8 -*-


##########################################################################################
# Importing packages. ####################################################################

import numpy as np
import csv
import re
import os
import ast
import math
import sympy as sp
import scipy as sc
from scipy import stats
import sys
import time

from termcolor import colored, cprint
import subprocess
from subprocess import DEVNULL, STDOUT, check_call

from sympy.parsing.sympy_parser import (parse_expr,standard_transformations,
                                        implicit_multiplication)
transformations = standard_transformations + (implicit_multiplication,)
separ = '--------------------------------------------'
sectspa = '                             '

##########################################################################################



##########################################################################################
# Variable extractor class and function. #################################################

class IdentifierExtractor(ast.NodeVisitor):
    def __init__(self):
        self.ids = set()
    def visit_Name(self, node):
        self.ids.add(node.id)


def VariableExtractor(FUN):
    extractor = IdentifierExtractor()
    extractor.visit(ast.parse(FUN))
    extractor.ids = extractor.ids - set(vars(math))
    return extractor.ids

##########################################################################################



##########################################################################################
# Round uncertainty functions. ###########################################################

def NumPow(X):
    Y = np.around(np.log10(abs(X)));
    Y = Y - (10 ** Y > abs(X));
    return Y

def UncRound(x, ux):

    if type(x) is float:
        x = np.array([[x]])
        ux = np.array([[ux]])
    elif type(x) is int:
        x = np.array([[x]])
        ux = np.array([[ux]])
    elif type(x) is np.ndarray:
        try:
            x.shape[1]
        except:
            x = x[:, np.newaxis]
            ux = ux[:, np.newaxis]

    n = NumPow(ux)
    Y = np.concatenate((x / (10 ** n), ux / (10 ** n)), axis=1)
    Y = np.concatenate((n, np.around(10 * Y) / 10), axis=1)

    # Correction if exact decimal in round.
    f, c = Y.shape
    for l in range(0, f):
        if Y[l][2] == 10:
            naux = n[l] + 1; xaux = x[l][0]; uxaux = ux[l][0]
            yaux = np.array([xaux, uxaux])
            Y[l] = np.concatenate((naux, np.around(10*yaux)/10), axis=0)
    return Y

def UncPrint(x, ux):
    try:
        aux1 = UncRound(x, ux)
        print('  ' + str(aux1[1]) + '(' + str(aux1[2]) + ') x 10[' + str(aux1[0]) + ']')
    except:
        aux1 = UncRound(x, ux); aux1 = aux1[0]
        print('  ' + str(aux1[1]) + '(' + str(aux1[2]) + ') x 10[' + str(aux1[0]) + ']')

##########################################################################################



##########################################################################################
# Export table to LaTeX document. ########################################################

def TableToTeX(MAT, CAP, SYM, UNI, ppath):
    f, c = MAT.shape
    C = np.zeros([f, int((3 / 2) * (c))], )

    for l in range(1, c, 2):
        B = UncRound(MAT[:, [l - 1]], MAT[:, [l]])
        C[:, [int((3 / 2) * (l + 1) - 3)]] = B[:, [0]]
        C[:, [int((3 / 2) * (l + 1) - 2)]] = B[:, [1]]
        C[:, [int((3 / 2) * (l + 1) - 1)]] = B[:, [2]]

    with open(ppath + 'export_TeX' + '.txt', 'a') as aux:
        aux.write('\\begin{table}[H] \n\\centering\n')
        aux.write('\\begin{tabular}{|')

        for m in range(0, int((1 - 1 / 2) * c)):
            aux.write('c|')
        aux.write('} \\hline\n')

        # Headings.
        for n in range(0, int(c / 2)):
            if n == c / 2 - 1:
                aux.write('$ ' + SYM[n] + ' \\ \\mathrm{(' + UNI[n] + ')} $')
                aux.write('\\\\ \\hline \\hline\n')
            else:
                aux.write('$ ' + SYM[n] + ' \\ \\mathrm{(' + UNI[n] + ')} $ & ')

        # All rows and cols iterative.
        for o in range(0, f):
            for p in range(0, int(3 * c / 2 - 2), 3):
                if p == int(3 * c / 2 - 3):
                    if C[o, [int(p)]] == -np.inf:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' \
                                  + str(float(C[o, [int(p + 2)]])) + \
                                  ' ) \\times 10^{\\infty} $ ')
                    else:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' \
                                  + str(float(C[o, [int(p + 2)]])) + \
                                  ' ) \\times 10^{' + str(int(C[o, [int(p)]])) + '} $ ')
                else:
                    if C[o, [int(p)]] == -np.inf:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' \
                                  + str(float(C[o, [int(p + 2)]])) + \
                                  ' ) \\times 10^{\\infty} $ & ')
                    else:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' \
                                  + str(float(C[o, [int(p + 2)]])) + \
                                  ' ) \\times 10^{' + str(int(C[o, [int(p)]])) + '} $ & ')
            aux.write('\\\\ \\hline\n')

        # Final activities: caption and ending enviroment.
        aux.write('\\end{tabular}\n\\caption{' + CAP + '}\n\\end{table}\n\n\n\n')

##########################################################################################



##########################################################################################
# Preview LaTeX table. ###################################################################

def PreviewTableTeX(MAT, CAP, SYM, UNI, ppath):
    f, c = MAT.shape
    C = np.zeros([f, int((3 / 2) * (c))], )

    for l in range(1, c, 2):
        B = UncRound(MAT[:, [l - 1]], MAT[:, [l]])
        C[:, [int((3 / 2) * (l + 1) - 3)]] = B[:, [0]]
        C[:, [int((3 / 2) * (l + 1) - 2)]] = B[:, [1]]
        C[:, [int((3 / 2) * (l + 1) - 1)]] = B[:, [2]]

    with open(ppath + 'preview_TeX' + '.tex', 'w') as aux:
        aux.write('\\documentclass[varwidth=true,border=10pt,convert={size=640x}]{standalone}\n')
        aux.write('\\usepackage{graphicx,float}\n')
        aux.write('\\usepackage[utf8]{inputenc}')
        aux.write('\\usepackage[T1]{fontenc}\n')
        aux.write('\\begin{document}\n')
        aux.write('\\begin{table}[H] \n\\centering\n')
        aux.write('\\resizebox{12cm}{!}{\\begin{tabular}{|')

        for m in range(0, int((1 - 1 / 2) * c)):
            aux.write('c|')
        aux.write('} \\hline\n')

        # Headings.
        for n in range(0, int(c / 2)):
            if n == c / 2 - 1:
                aux.write('$ ' + SYM[n] + ' \\ \\mathrm{(' + UNI[n] + ')} $')
                aux.write('\\\\ \\hline \\hline\n')
            else:
                aux.write('$ ' + SYM[n] + ' \\ \\mathrm{(' + UNI[n] + ')} $ & ')

        # All rows and cols iterative.
        for o in range(0, f):
            for p in range(0, int(3 * c / 2 - 2), 3):
                if p == int(3 * c / 2 - 3):
                    if C[o, [int(p)]] == -np.inf:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' + str(float(C[o, [int(p + 2)]])) + ' ) \\times 10^{\\infty} $ ')
                    else:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' + str(float(C[o, [int(p + 2)]])) + ' ) \\times 10^{' + str(int(C[o, [int(p)]])) + '} $ ')
                else:
                    if C[o, [int(p)]] == -np.inf:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' + str(float(C[o, [int(p + 2)]])) + ' ) \\times 10^{\\infty} $ & ')
                    else:
                        aux.write('$ ( ' + str(float(C[o, [int(p + 1)]])) + ' \\pm ' + str(float(C[o, [int(p + 2)]])) + ' ) \\times 10^{' + str(int(C[o, [int(p)]])) + '} $ & ')
            aux.write('\\\\ \\hline\n')

        # Final activities: caption and ending enviroment.
        aux.write('\\end{tabular}}\n\\caption{'+CAP+'}\n\\end{table}\n\\end{document}\n')

    # Comppiling
    check_call(['/usr/local/texlive/2017/bin/x86_64-darwin/pdflatex', ppath + 'preview_TeX.tex'], stdout=DEVNULL, stderr=STDOUT)
    os.system('rm preview_TeX.log')
    os.system('rm preview_TeX.aux')
    os.system('rm ' + ppath + 'preview_TeX.tex')
    #os.system('open -a Preview.app ' + '/Users/marcos/Documents/Python/ProjectMaker/' + 'preview_TeX.pdf')
    os.system('open preview_TeX.pdf')
    os.system('rm preview_TeX.pdf')
##########################################################################################



##########################################################################################
# Wolfram. ###############################################################################

def WolframEx(MAT, CAP, SYM, UNI, ppath):
    f, c = MAT.shape

    if c==4:
        with open(ppath + 'export_WMT' + '.txt', 'a') as aux:
            aux.write(separ + 'x' + separ + '\n\n$PlotTheme = "Classic";\nNeeds["ErrorBarPlots`"];\n\n')

            # Points.
            aux.write('data={\n'); p = 0
            for l in range(0, f):
                if l == int(f - 1):
                    aux.write('{' + str(float(MAT[l, [int(p + 0)]])) + ',' + str(float(MAT[l, [int(p + 2)]])) +'}')
                else:
                    aux.write('{' + str(float(MAT[l, [int(p + 0)]])) + ',' + str(float(MAT[l, [int(p + 2)]])) + '},\n')
            aux.write('};\n\n')

            # Errorbars.
            aux.write('EL=ErrorListPlot[{\n'); p = 0
            for o in range(0, f):
                if o == int(f-1):
                    aux.write('{{' + str(float(MAT[o, [int(p + 0)]])) + ',' + str(float(MAT[o, [int(p + 2)]])) + '},ErrorBar[' + str(float(MAT[o, [int(p + 1)]])) + ',' + str(float(MAT[o, [int(p + 3)]])) + ']}')
                else:
                    aux.write('{{' + str(float(MAT[o, [int(p + 0)]])) + ',' + str(float(MAT[o, [int(p + 2)]])) + '},ErrorBar[' + str(float(MAT[o, [int(p + 1)]])) + ',' + str(float(MAT[o, [int(p + 3)]])) + ']},\n')
            aux.write('}];\n\n')

            # Final activities: caption and ending enviroment.
            aux.write('LP = ListPlot[data];\n')
            aux.write('LL = ListLinePlot[data];\n')
            aux.write('Show[LP, LL, Frame -> True, FrameLabel -> {"' + SYM[0] + '(' + UNI[0] + ')", "' + SYM[1] + '(' + UNI[1] + ')"},AspectRatio -> 1 / GoldenRatio]\n\n')
    else:
        print('  Exporter can not export the selected data to Wolfram: bad selection.')

##########################################################################################



##########################################################################################
# Load ALL variables in a database. ######################################################

def LoadVar(ppath, database):
    file = ppath + str(database) + '.csv';
    Data = {}
    if os.path.isfile(file) is True:
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            q = list(spamreader)
        print('# Loading ' + str(file) + '.')
        aux = np.zeros(len(q[0]) - 2, )
        for l in range(0, len(q)):
            row = q[l]; nam = q[0]
            if l == 0:
                for m in range(0,int(len(row)/2)):
                    Data[str(row[2*m])] = {}
            elif l == 1:
                for m in range(0,int(len(row)/2)):
                    Data[str(nam[2*m])]['sym'] = row[2*m+0]
                    Data[str(nam[2*m])]['uni'] = row[2*m+1]
                    Data[str(nam[2*m])]['dat'] = np.zeros(len(q)-2,)
                    Data[str(nam[2*m])]['unc'] = np.zeros(len(q)-2,)
            else:
                for m in range(0,int(len(row)/2)):
                    if row[2*m+0] != '':
                        Data[str(nam[2*m])]['dat'][l-2] = float(row[2*m+0])
                    else:
                        Data[str(nam[2*m])]['dat'] = \
                            np.delete(Data[str(nam[2*m])]['dat'], \
                                      l - 2 - aux[m - 1])
                    if row[2*m+1] != '':
                        Data[str(nam[2*m])]['unc'][l - 2] = \
                            float(row[2*m+1])
                    else:
                        Data[str(nam[2*m])]['unc'] = \
                            np.delete(Data[str(nam[2*m])]['unc'], \
                                      l - 2 - aux[m - 1])
                        aux[m - 1] = aux[m - 1] + 1
        print('  Load file success.')
        if len(Data) is 0:
            print('  Nothing to load.')
            Data = {}
    else:
        print('  Database does not exist!')
        Data = {}
    return Data

##########################################################################################



##########################################################################################
# Store ONE variable in a database. ######################################################

def StoreVar(vardata, varname, ppath, database):
    Data = LoadVar(ppath,database)
    print('  Creating label in database dictionary.')
    Data[str(varname)] = vardata

    # Searching the biggest vector in Data
    aux1 = 0
    for l in range(0, len(Data.keys())):
        aux1 = max(len(Data[list(Data.keys())[l]]['dat']), aux1)

    # Headers of data table
    for l in range(0, len(Data.keys())):
        if len(Data.keys()) == 1:
            aux = list(Data.keys())[l]
            rowNAME = str(aux) + ',' + ' ' + '\n'
            rowSYUN = str(Data[list(Data.keys())[l]]['sym']) + ',' + \
                      str(Data[list(Data.keys())[l]]['uni']) + '\n'
            print('  Variable name(s) are stored.')
        else:
            if l == 0:
                aux = list(Data.keys())[l]
                rowNAME = str(aux) + ',' + ' '
                rowSYUN = str(Data[list(Data.keys())[l]]['sym']) + ',' + \
                          str(Data[list(Data.keys())[l]]['uni'])
                print('  Variable symbols and units are stored.')
            elif l == len(Data.keys()) - 1:
                aux = list(Data.keys())[l]
                rowNAME = rowNAME + ',' + str(aux) + ',' + ' ' + '\n'
                rowSYUN = rowSYUN + ',' + \
                          str(Data[list(Data.keys())[l]]['sym']) + ',' + \
                          str(Data[list(Data.keys())[l]]['uni']) + '\n'
            else:
                aux = list(Data.keys())[l]
                rowNAME = rowNAME + ',' + str(aux) + ',' + ' '
                rowSYUN = rowSYUN + ',' + Data[list(Data.keys())[l]]['sym'] + \
                          ',' + Data[list(Data.keys())[l]]['uni']

    with open(ppath + database + '.csv', 'w') as aux:
        aux.write(rowNAME)
        aux.write(rowSYUN)

        # Writing data and uncertainty row by row
        for l in range(0, max(aux1, len(vardata['dat']))):
            for m in range(0, len(Data.keys())):
                if len(Data.keys()) == 1:  # 1 var
                    rowDAUN = str(float(Data[list(Data.keys())[m]]['dat'][l])) + \
                              ',' + str(float(Data[list(Data.keys())[m]]['unc'][l])) + '\n'
                    aux.write(rowDAUN)
                else:
                    if m == 0:
                        if l <= len((Data[list(Data.keys())[m]]['dat'])) - 1:
                            rowDAUN = \
                                str(float(Data[list(Data.keys())[m]]['dat'][l])) + ',' + \
                                str(float(Data[list(Data.keys())[m]]['unc'][l]))
                        else:
                            rowDAUN = \
                                '' + ',' + \
                                ''
                    elif m == len(Data.keys()) - 1:
                        if l <= len((Data[list(Data.keys())[m]]['dat'])) - 1:
                            rowDAUN = rowDAUN + ',' + \
                                      str(float(Data[list(Data.keys())[m]]['dat'][l])) + ',' + \
                                      str(float(Data[list(Data.keys())[m]]['unc'][l])) + '\n'
                        else:
                            rowDAUN = rowDAUN + ',' + \
                                      '' + ',' + \
                                      '' + '\n'
                        aux.write(rowDAUN)
                    else:
                        if l <= len((Data[list(Data.keys())[m]]['dat'])) - 1:
                            rowDAUN = rowDAUN + ',' + \
                                      str(float(Data[list(Data.keys())[m]]['dat'][l])) + ',' + \
                                      str(float(Data[list(Data.keys())[m]]['unc'][l]))
                        else:
                            rowDAUN = rowDAUN + ',' + \
                                      '' + ',' + \
                                      ''
    print('  Variable data and uncertainty are stored.')

##########################################################################################



##########################################################################################
# Disp a ProjectMaker variable. ##########################################################

def dispu(var):
    try:
        aux1 = ''; aux2 = ''; aux3 = ''
        for l in range(0,len(var)):
            aux1 = aux1 + 'Var[' + str(l+1) + '] - Symbol: ' + var[l]["sym"] + '\n'
            aux1 = aux1 + 'Var[' + str(l+1) + '] - Units : ' + var[l]["uni"] + '\n'
            aux2 = aux2 + 'd({})'.format(var[l]["sym"]).rjust(12)
            aux2 = aux2 + 'u({})'.format(var[l]["sym"]).rjust(12)
            aux3 = aux3 + '{}'.format('-').rjust(12,'-')
            aux3 = aux3 + '{}'.format('-').rjust(12,'-')
            try:
                len(var[l]['dat']) == len(var[0]['dat'])
            except:
                print('Variables have not the same lenght. So no printing.')
        print('Variables to print metadata.')
        print('The number of events is ' + str(len(var[0]['dat'])))
        print(aux1); print(aux3); print(aux2); print(aux3)

        for m in range(0, len(var[0]['dat'])):
            aux4 = ''
            for l in range(0,len(var)):
                aux4 = aux4 + '{}'.format(str(var[l]["dat"][m])).rjust(12)
                aux4 = aux4 + '{}'.format(str(var[l]["unc"][m])).rjust(12)
            print(aux4)
        print(aux3 + '\n')
    except:
        print('Status Failure.')

def disp(var):
    try:
        aux1 = ''; aux2 = ''; aux3 = ''
        for l in range(0,len(var)):
            aux1 = aux1 + 'Var[' + str(l+1) + '] - Symbol: ' + var[l]["sym"] + '\n'
            aux1 = aux1 + 'Var[' + str(l+1) + '] - Units : ' + var[l]["uni"] + '\n'
            aux2 = aux2 + 'd({})'.format(var[l]["sym"]).rjust(15)
            aux3 = aux3 + '{}'.format('-').rjust(15,'-')
            try:
                len(var[l]['dat']) == len(var[0]['dat'])
            except:
                print('Variables have not the same lenght. So no printing.')
        print('Variables to print metadata.')
        print('The number of events is ' + str(len(var[0]['dat'])))
        print(aux1); print(aux3); print(aux2); print(aux3)

        for m in range(0, len(var[0]['dat'])):
            aux4 = ''
            for l in range(0,len(var)):
                aux4 = aux4 + '{}'.format(str(var[l]["dat"][m])).rjust(15)
            print(aux4)
        print(aux3 + '\n')
    except:
        print('Status Failure.')

##########################################################################################

def SetUp():
    print('Setting Current Path is needed. Set it writting:')
    print('CURRENTPATH = "your/path"\n')
    aux1 = 'Each time your database is modified you must refresh Data variable.'
    aux2 = 'The very first time importing database is compulsury. This can be done as:'
    aux3 = 'Data = LoadVar(ppath,"Data")'
    print(aux1 + aux2 + '\n' + aux3 + '\n')

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def read_from_clipboard():
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')