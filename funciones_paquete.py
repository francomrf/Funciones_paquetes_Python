# -*- coding: utf-8 -*-
#reset -f
"""
Created on Wed Apr  6 15:11:37 2022

@author: Franco Fabián
"""

'''Ejemplos'''

def saludo1():
    x='Hola MINEDU'
    return x

saludo1()

def saludo2():
    print('Hola MINEDU')

saludo2()

def adición(a,b):
    x=a+b
    return x

adición(3,2)

'''
    Área: Unidad de Planificación y Presupuesto - Equipo Data
    Objetivos: Costear JEC

        ETAPA 0: Preparar e importar librerías

        ETAPA 1: Definir variables para remuneración

            a) Períodos de tiempo
            b) Remuneraciones

        ETAPA 2: Definir funciones

        ETAPA 3: Estimación del Padrón

            a) Importar Padrón Escale e Intervención
            b) Exportar Padrón

        ETAPA 4: Estimación de PEAS

            a) Estimar meta
            b) Exportar PEAS

        ETAPA 5: Cálculo de PxQ con funciones

            a) Cálculo de contratación CAS
            b) Cálculo de aguinaldo
            c) Cálculo de EsSalud
            d) Cálculo de montos totales

        ETAPA 6: Cálculo de PxQ con paquete de costeo

            a) Cálculo de contratación CAS
            b) Cálculo de aguinaldo
            c) Cálculo de EsSalud
            d) Cálculo de montos totales

'''

'''
        ETAPA 0: Preparar e importar librerías

'''

# Ruta del directorio: D:\

ruta='D:\presentaciones\pyfunciones'

# Ruta de archivos de entrada: D:+\Input

ruta_input=ruta+'\Input'

# Ruta de archivos de salida: D:+\Output

ruta_output=ruta+'\Output'

# Importar librería Pandas

import pandas as pd

import numpy as np

import math

'''
        ETAPA 1: Definir variables para remuneración

'''

# a) Períodos de tiempo

# Número de meses: 12 y 10 meses

m_12=12
m_10=10

# Número de veces que se recibe aguinaldo

agui_1=1
agui_2=2

# Perfiles:

#Coordinador(a) de innovación y soporte tecnológico (12 y 10 meses)
#Psicólogo(a) (12 y 10 meses)
#Personal de mantenimiento (12 y 10 meses)
#Personal de vigilancia (12 meses)

# Lista de meses

mes_13=['ene','feb','mar','abr','may','jun','jul','ago','set','oct','nov','dic','anual']
mes_12=['ene','feb','mar','abr','may','jun','jul','ago','set','oct','nov','dic']
mes_10=['mar','abr','may','jun','jul','ago','set','oct','nov','dic']
mes_inactivo_2=['ene','feb']
mes_agui_2=['jul','dic']
mes_noagui_2=['ene','feb','mar','abr','may','jun','ago','set','oct','nov']

# b) Remuneraciones

# Monto Promotores de bienestar

# Monto de Coordinador(a) de innovación y soporte tecnológico

monto_cist=1350

# Monto de Psicólogo(a)

monto_psi=2500

# Monto de Personal de mantenimiento

monto_mant=1150

# Monto de Personal de vigilancia

monto_vig=1150

# Monto aguinaldo 2 veces al año

monto_agui=300

# Monto UIT

UIT=4600

# Porcentaje de la UIT

UIT_porc=0.55

'''
        ETAPA 2: Definir funciones

'''

def cas(nombre_perfil,meses_perfil,monto_perfil):

    bint['cas_'+nombre_perfil+'_anual'] = bint[nombre_perfil]*meses_perfil*monto_perfil

    if meses_perfil == 12:

        for mes in mes_12:
            bint['cas_'+nombre_perfil+'_'+mes] = bint[nombre_perfil]*monto_perfil

    else:

        for mes in mes_10:
            bint['cas_'+nombre_perfil+'_'+mes] = bint[nombre_perfil]*monto_perfil

        for mes in mes_inactivo_2:
            bint['cas_'+nombre_perfil+'_'+mes] = 0

#cas('psi_10',m_10,monto_psi)

# Aguinaldo

# nombre_perfil: nombre del perfil, entre comillas
# veces_agui: número de veces que recibe aguinaldo
# monto_agui: monto del aguinaldo

def aguinaldo(nombre_perfil,veces_agui,monto_agui):

    bint['agui_'+nombre_perfil+'_anual'] = bint[nombre_perfil]*veces_agui*monto_agui

    for mes in mes_agui_2:
        bint['agui_'+nombre_perfil+'_'+mes] = bint[nombre_perfil]*monto_agui

    for mes in mes_noagui_2:
        bint['agui_'+nombre_perfil+'_'+mes] = 0

#aguinaldo('vig',agui_2,monto_agui)

# Tope de Essalud

# UIT_porc: Porcentaje de UIT
# UIT: UIT del año

def tope(UIT_porc,UIT):
    x=math.ceil(0.09*UIT_porc*UIT)
    return x

#monto_tope=tope(0.55,4600)

# Aporte individual a EsSalud

# nombre_perfil: nombre del perfil, entre comillas
# monto_perfil: monto del perfil
# monto_tope: monto de top de EsSalud, hallada con la función tope

def aporte_essalud(nombre_perfil,monto_perfil,monto_tope):

    bint['ess_'+nombre_perfil] = min(math.ceil(0.09*monto_perfil),monto_tope)

#aporte_essalud('mant', monto_vig, monto_tope)

# EsSalud

# nombre_perfil: nombre del perfil, entre comillas
# meses_perfil: número de meses activos del perfil


def essalud(nombre_perfil,meses_perfil):

    bint['essalud_'+nombre_perfil+'_anual'] = bint[nombre_perfil]*meses_perfil*bint['ess_'+nombre_perfil]

    if meses_perfil == 12:

        for mes in mes_12:
            bint['essalud_'+nombre_perfil+'_'+mes] = bint[nombre_perfil]*bint['ess_'+nombre_perfil]

    else:

        for mes in mes_10:
            bint['essalud_'+nombre_perfil+'_'+mes] = bint[nombre_perfil]*bint['ess_'+nombre_perfil]

        for mes in mes_inactivo_2:
            bint['essalud_'+nombre_perfil+'_'+mes] = 0

# Total por perfil

# nombre: puede tomar los valores = cas, ess, agui
# nombre_perfil: nombre del perfil, entre comillas
# continuidad: si el perfil cuenta con continuidad, puede tomar valores = 1, 2
# 1: perfil con solo contrato de 12 meses o solo 10 meses
# 2: perfil con contrato de 12 meses y 10 meses

def total_perfil(nombre,nombre_perfil,continuidad):

    if continuidad == 1:
        bint[nombre+'_'+nombre_perfil+'_total'] = bint[nombre+'_'+nombre_perfil+'_anual']

    if continuidad == 2:
        bint[nombre+'_'+nombre_perfil+'_total'] = bint[nombre+'_'+nombre_perfil+'_anual']+bint[nombre+'_'+nombre_perfil+'_10_anual']

# Total por perfil por meses

# nombre: puede tomar los valores = cas, ess, agui
# nombre_perfil: nombre del perfil, entre comillas
# continuidad: si el perfil cuenta con continuidad, puede tomar valores = 1, 2
# 1: perfil con solo contrato de 12 meses o solo 10 meses
# 2: perfil con contrato de 12 meses y 10 meses

def total_perfil_mes(nombre,nombre_perfil,continuidad):

    if continuidad == 1:

        for mes in mes_12:
            bint[nombre+'_'+nombre_perfil+'_total_'+mes] = bint[nombre+'_'+nombre_perfil+'_'+mes]

    if continuidad == 2:

        for mes in mes_12:
            bint[nombre+'_'+nombre_perfil+'_total_'+mes] = bint[nombre+'_'+nombre_perfil+'_'+mes]+bint[nombre+'_'+nombre_perfil+'_10_'+mes]

# Totales

# nombre: puede tomar los valores = cas, ess, agui, costo
# cas: costo total de CAS de todos los perfiles
# ess: costo total de EsSalud de todos los perfiles
# agui: costo total de aguinaldo de todos los perfiles
# costo: suma de CAS, EsSalud y aguinaldo

def total(nombre):

    if nombre == 'cas':
        bint['total_'+nombre+'_admin'] = bint[bint.columns[[x.startswith('cas_') for x in bint.columns]].tolist()].sum(axis=1)
    elif nombre == 'ess':
        bint['total_'+nombre+'_admin'] = bint[bint.columns[[x.startswith('essalud_') for x in bint.columns]].tolist()].sum(axis=1)
    elif nombre == 'agui':
        bint['total_'+nombre+'_admin'] = bint[bint.columns[[x.startswith('agui_') for x in bint.columns]].tolist()].sum(axis=1)
    else:
        bint[nombre+'_cas_admin'] = bint[bint.columns[[x.startswith('total_') for x in bint.columns]].tolist()].sum(axis=1)

# Total por mes

# nombre: puede tomar los valores = cas, ess, agui
# cas: costo total de CAS de todos los perfiles por mes
# ess: costo total de EsSalud de todos los perfiles por mes
# agui: costo total de aguinaldo de todos los perfiles por mes

def total_mes(nombre):

    if nombre == 'cas':
        bcas = bint[bint.columns[[x.startswith('cas_') for x in bint.columns]].tolist()]
        bint['cas_admin_ene'] = bcas[bcas.columns[[x.endswith('_ene') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_feb'] = bcas[bcas.columns[[x.endswith('_feb') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_mar'] = bcas[bcas.columns[[x.endswith('_mar') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_abr'] = bcas[bcas.columns[[x.endswith('_abr') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_may'] = bcas[bcas.columns[[x.endswith('_may') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_jun'] = bcas[bcas.columns[[x.endswith('_jun') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_jul'] = bcas[bcas.columns[[x.endswith('_jul') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_ago'] = bcas[bcas.columns[[x.endswith('_ago') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_set'] = bcas[bcas.columns[[x.endswith('_set') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_oct'] = bcas[bcas.columns[[x.endswith('_oct') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_nov'] = bcas[bcas.columns[[x.endswith('_nov') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_dic'] = bcas[bcas.columns[[x.endswith('_dic') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['cas_admin_anual'] = bcas[bcas.columns[[x.endswith('_anual') for x in bcas.columns]].tolist()].sum(axis=1)

    elif nombre == 'ess':
        bcas = bint[bint.columns[[x.startswith('essalud_') for x in bint.columns]].tolist()]
        bint['ess_admin_ene'] = bcas[bcas.columns[[x.endswith('_ene') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_feb'] = bcas[bcas.columns[[x.endswith('_feb') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_mar'] = bcas[bcas.columns[[x.endswith('_mar') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_abr'] = bcas[bcas.columns[[x.endswith('_abr') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_may'] = bcas[bcas.columns[[x.endswith('_may') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_jun'] = bcas[bcas.columns[[x.endswith('_jun') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_jul'] = bcas[bcas.columns[[x.endswith('_jul') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_ago'] = bcas[bcas.columns[[x.endswith('_ago') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_set'] = bcas[bcas.columns[[x.endswith('_set') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_oct'] = bcas[bcas.columns[[x.endswith('_oct') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_nov'] = bcas[bcas.columns[[x.endswith('_nov') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_dic'] = bcas[bcas.columns[[x.endswith('_dic') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['ess_admin_anual'] = bcas[bcas.columns[[x.endswith('_anual') for x in bcas.columns]].tolist()].sum(axis=1)

    else:
        bcas = bint[bint.columns[[x.startswith('agui_') for x in bint.columns]].tolist()]
        bint['agui_admin_ene'] = bcas[bcas.columns[[x.endswith('_ene') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_feb'] = bcas[bcas.columns[[x.endswith('_feb') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_mar'] = bcas[bcas.columns[[x.endswith('_mar') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_abr'] = bcas[bcas.columns[[x.endswith('_abr') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_may'] = bcas[bcas.columns[[x.endswith('_may') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_jun'] = bcas[bcas.columns[[x.endswith('_jun') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_jul'] = bcas[bcas.columns[[x.endswith('_jul') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_ago'] = bcas[bcas.columns[[x.endswith('_ago') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_set'] = bcas[bcas.columns[[x.endswith('_set') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_oct'] = bcas[bcas.columns[[x.endswith('_oct') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_nov'] = bcas[bcas.columns[[x.endswith('_nov') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_dic'] = bcas[bcas.columns[[x.endswith('_dic') for x in bcas.columns]].tolist()].sum(axis=1)
        bint['agui_admin_anual'] = bcas[bcas.columns[[x.endswith('_anual') for x in bcas.columns]].tolist()].sum(axis=1)

'''
        ETAPA 3: Estimación del Padrón

'''

# Importar PEAS

peas=pd.read_excel(ruta_input+'/Peas.xlsx',sheet_name='Sheet1',nrows=2001,header=3)

# Renombrar

peas.rename(columns={'Nombre del Centro Educativo':'nom_iiee'},inplace=True)
peas.rename(columns={'Código Modular':'cod_mod'},inplace=True)
peas.rename(columns={'Anexo':'anexo'},inplace=True)

# Importar Padrón web

pad=pd.read_excel(ruta_input+'/Padron.xlsx')

# Ordenar variables de interés

pad_i=pad[['cod_mod','anexo','cen_edu','d_dreugel','codooii','d_estado','d_gestion','d_dpto','d_prov','d_dist','cen_pob','niv_mod','total_alumnos','total_profes','tseccion']]

# Combinar bases usando inner

peas_pad=pd.merge(peas, pad_i, on =['cod_mod','anexo'], how ="inner")

# Renombrar

peas_pad.rename(columns={'d_dreugel':'dre_ugel'},inplace=True)
peas_pad.rename(columns={'codooii':'cod_ugel'},inplace=True)
peas_pad.rename(columns={'Código Local':'cod_local'},inplace=True)
peas_pad.rename(columns={'tseccion':'total_secciones'},inplace=True)
peas_pad.rename(columns={'Coordinador(a) de Innovación y Soporte Tecnológico':'cist'},inplace=True)
peas_pad.rename(columns={'Psicólogo(a)':'psi'},inplace=True)
peas_pad.rename(columns={'Personal de Mantenimiento':'mant'},inplace=True)
peas_pad.rename(columns={'Personal de Vigilancia':'vig'},inplace=True)

# Arreglo para caracteres especiales

# Generar iiee

peas_pad.loc[(peas_pad['cen_edu'] == peas_pad['nom_iiee']),'iiee_vs'] = 1

# Reemplzar NA por 0

peas_pad = peas_pad.fillna(0)

# Importar base UE UGEL

ue=pd.read_excel(ruta_input+'/Base UE UGEL.xlsx',sheet_name='Versión Actualizada',header=0)

# Renombrar

ue.rename(columns={'COD_PLIEGO':'cod_pliego'},inplace=True)
ue.rename(columns={'COD_UE':'cod_ue'},inplace=True)
ue.rename(columns={'PLIEGO':'nom_pliego'},inplace=True)
ue.rename(columns={'EJECUTORA':'nom_ue'},inplace=True)

# Eliminar cod_ugel=na

ue = ue.dropna(subset=['cod_ugel'])

# Eliminar colegios militares

ue.drop(ue[ue['nom_ue'].str.contains('301. COLEGIO MILITAR')].index, inplace=True)

# Verificar tipo de variables

print(peas_pad.dtypes)
print(ue.dtypes)

# Pasar a int

peas_pad.cod_ugel=peas_pad.cod_ugel.astype(int)
ue.cod_ugel=ue.cod_ugel.astype(int)

# Combinar bases: padrón y base UE UGEL

peas_pad_ue=pd.merge(peas_pad, ue, on =['cod_ugel'], how ="inner")

peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 209973), 'cod_ue'] = 301
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 209973), 'nom_ue'] = '301. COLEGIO MILITAR LEONCIO PRADO'
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 209973), 'cod_pliego'] = 464
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 209973), 'nom_pliego'] = '464. GOBIERNO REGIONAL DE LA PROVINCIA CONSTITUCIONAL DEL CALLAO'

peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 512251), 'cod_ue'] = 301
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 512251), 'nom_ue'] = '301. COLEGIO MILITAR PEDRO RUIZ GALLO'
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 512251), 'cod_pliego'] = 457
peas_pad_ue.loc[(peas_pad_ue['cod_mod'] == 512251), 'nom_pliego'] = '457. GOBIERNO REGIONAL DEL DEPARTAMENTO DE PIURA'

# Ordenar por variables

peas_pad_ue_sort=peas_pad_ue.sort_values(by=['cod_pliego','cod_ue','cod_mod','cod_local'])

# Establecer df con variables de interés

padron=peas_pad_ue_sort[['nom_pliego','nom_ue','ugel','cod_mod','anexo','cod_local','nom_iiee']]

# Cambiar cod_mod a str

padron.cod_mod=padron.cod_mod.astype(str)

# Agregar 0 a la izquierda

padron['cod_mod']= padron['cod_mod'].str.zfill(7)

# Renombrar

padron.rename(columns={'nom_pliego':'Pliego'},inplace=True)
padron.rename(columns={'nom_ue':'Unidad Ejecutora'},inplace=True)
padron.rename(columns={'ugel':'UGEL'},inplace=True)
padron.rename(columns={'cod_mod':'Código Modular'},inplace=True)
padron.rename(columns={'anexo':'Anexo'},inplace=True)
padron.rename(columns={'cod_local':'Código Local'},inplace=True)
padron.rename(columns={'nom_iiee':'Nombre del Centro Educativo'},inplace=True)

# Exportar Padrón

padron.to_excel(ruta_output+'/Padrón JEC vtest.xlsx', sheet_name='Padrón' , index= False)

'''
        ETAPA 4: Estimación de PEAS

'''

# Cantidad meta para formato MEF

peas_pad_ue['iiee']=1

# Agrupar a nivel de cod_mod, cod_ue, cod_ugel (collapse)

meta=peas_pad_ue.groupby(['cod_pliego','nom_pliego','cod_ue','nom_ue','cod_ugel','ugel'])[['iiee']].sum().reset_index()

# Generar PEAS a nivel de código modular

# Renombrar

peas_pad_ue.rename(columns={'iiee':'n_IIEE'},inplace=True)

# Establecer df con variables de interés

peascod=peas_pad_ue[['cod_pliego','nom_pliego','cod_ue','nom_ue','cod_ugel','ugel','cod_mod','anexo','nom_iiee','cod_local','total_alumnos','total_profes','total_secciones','n_IIEE','cist','cist_10','psi','psi_10','mant','mant_10','vig']]

# Ordenar por variables

peascod_sort=peascod.sort_values(by=['cod_ue','cod_ugel','cod_mod','cod_local'])

# Cambiar cod_mod a str

peascod_sort.cod_mod=peascod_sort.cod_mod.astype(str)

# Agregar 0 a la izquierda

peascod_sort['cod_mod']= peascod_sort['cod_mod'].str.zfill(7)

# Renombrar

peascod_sort.rename(columns={'cod_pliego':'Código de Pliego'},inplace=True)
peascod_sort.rename(columns={'nom_pliego':'Pliego'},inplace=True)
peascod_sort.rename(columns={'cod_ue':'Código de Unidad Ejecutora'},inplace=True)
peascod_sort.rename(columns={'nom_ue':'Unidad Ejecutora'},inplace=True)
peascod_sort.rename(columns={'cod_ugel':'Código de UGEL'},inplace=True)
peascod_sort.rename(columns={'ugel':'Nombre de UGEL'},inplace=True)
peascod_sort.rename(columns={'cod_mod':'Código Modular'},inplace=True)
peascod_sort.rename(columns={'anexo':'Anexo'},inplace=True)
peascod_sort.rename(columns={'nom_iiee':'Nombre del Centro Educativo'},inplace=True)
peascod_sort.rename(columns={'cod_local':'Código Local'},inplace=True)
peascod_sort.rename(columns={'total_alumnos':'Total de alumnos SIAGIE'},inplace=True)
peascod_sort.rename(columns={'total_profes':'Total de profesores Nexus'},inplace=True)
peascod_sort.rename(columns={'total_secciones':'Total de secciones'},inplace=True)
peascod_sort.rename(columns={'cist':'Coordinador(a) de Innovación y Soporte Tecnológico'},inplace=True)
peascod_sort.rename(columns={'psi':'Psicólogo(a)'},inplace=True)
peascod_sort.rename(columns={'mant':'Personal de Mantenimiento'},inplace=True)
peascod_sort.rename(columns={'vig':'Personal de Vigilancia'},inplace=True)

# Exportar PEAS a nivel de código modular

peascod_sort.to_excel(ruta_output+'/peascod vtest.xlsx', sheet_name='PEAS' , index= False)

# Generar PEAS a nivel de UGEL

# Agrupar a nivel de cod_pliego, cod_ue, cod_ugel (collapse)

bint=peas_pad_ue.groupby(by=['cod_pliego','nom_pliego','cod_ue','nom_ue','cod_ugel','ugel'])[['total_alumnos','total_profes','n_IIEE','total_secciones','cist','cist_10','psi','psi_10','mant','mant_10','vig']].sum().reset_index()

# Generar vigilantes por UGEL

bint['vig_ugel'] = (bint['n_IIEE']/6).apply(np.ceil)

# Reemplazar por 3 vigilantes

bint.loc[(bint['cod_pliego'] == 456)&(bint['cod_ue'] == 301)&(bint['cod_ugel'] == 190003), 'vig_ugel'] = 3

# Establecer df con variables de interés

peasugel=bint[['cod_pliego','nom_pliego','cod_ue','nom_ue','cod_ugel','ugel','total_alumnos','total_profes','total_secciones','n_IIEE','vig_ugel']]

# Ordenar por variables

peasugel_sort=peasugel.sort_values(by=['cod_pliego','cod_ue','cod_ugel'])

# Renombrar

peasugel_sort.rename(columns={'cod_pliego':'Código de Pliego'},inplace=True)
peasugel_sort.rename(columns={'nom_pliego':'Pliego'},inplace=True)
peasugel_sort.rename(columns={'cod_ue':'Código de Unidad Ejecutora'},inplace=True)
peasugel_sort.rename(columns={'nom_ue':'Unidad Ejecutora'},inplace=True)
peasugel_sort.rename(columns={'cod_ugel':'Código de UGEL'},inplace=True)
peasugel_sort.rename(columns={'ugel':'Nombre de UGEL'},inplace=True)
peasugel_sort.rename(columns={'total_alumnos':'Total de alumnos SIAGIE'},inplace=True)
peasugel_sort.rename(columns={'total_profes':'Total de profesores Nexus'},inplace=True)
peasugel_sort.rename(columns={'total_secciones':'Total de secciones'},inplace=True)
peasugel_sort.rename(columns={'vig_ugel':'Personal de Vigilancia'},inplace=True)

# Exportar PEAS a nivel de UGEL

peasugel_sort.to_excel(ruta_output+'/peasugel vtest.xlsx', sheet_name='peasugel' , index= False)

# Cantidad de vigilantes

bint['vig'] = bint['vig']+bint['vig_ugel']

# Eliminar vigilantes por UGEL

del bint['vig_ugel']

'''
        ETAPA 5: Cálculo de PxQ con funciones

'''

# CAS y aguinaldo

cas('cist',m_12,monto_cist)
cas('cist_10',m_10,monto_cist)
cas('psi',m_12,monto_psi)
cas('psi_10',m_10,monto_psi)
cas('mant',m_12,monto_mant)
cas('mant_10',m_10,monto_mant)
cas('vig',m_12,monto_vig)

aguinaldo('cist', agui_2, monto_agui)
aguinaldo('cist_10', agui_2, monto_agui)
aguinaldo('psi',agui_2,monto_agui)
aguinaldo('psi_10', agui_2, monto_agui)
aguinaldo('mant', agui_2, monto_agui)
aguinaldo('mant_10', agui_2, monto_agui)
aguinaldo('vig', agui_2, monto_agui)

# EsSalud

monto_tope=tope(0.55,4600)

aporte_essalud('cist', monto_cist, monto_tope)
aporte_essalud('cist_10', monto_cist, monto_tope)
aporte_essalud('psi', monto_psi, monto_tope)
aporte_essalud('psi_10', monto_psi, monto_tope)
aporte_essalud('mant', monto_mant, monto_tope)
aporte_essalud('mant_10', monto_mant, monto_tope)
aporte_essalud('vig', monto_vig, monto_tope)

essalud('cist', m_12)
essalud('cist_10', m_10)
essalud('psi', m_12)
essalud('psi_10', m_10)
essalud('mant', m_12)
essalud('mant_10', m_10)
essalud('vig', m_12)

# Generar totales

total('cas')
total('ess')
total('agui')
total('costo')

total_mes('cas')
total_mes('ess')
total_mes('agui')

'''
        ETAPA 6: Cálculo de PxQ con paquete de costeo

'''

from costeopy_package import costeopy as ct

# CAS y aguinaldo

ct.cas(bint, 'cist', m_12, monto_cist)
ct.cas(bint, 'cist_10', m_10, monto_cist)
ct.cas(bint, 'psi', m_12, monto_psi)
ct.cas(bint, 'psi_10', m_10, monto_psi)
ct.cas(bint, 'mant', m_12, monto_mant)
ct.cas(bint, 'mant_10', m_10, monto_mant)
ct.cas(bint, 'vig', m_12, monto_vig)

ct.aguinaldo(bint, 'cist', agui_2, monto_agui)
ct.aguinaldo(bint, 'cist_10', agui_2, monto_agui)
ct.aguinaldo(bint, 'psi', agui_2, monto_agui)
ct.aguinaldo(bint, 'psi_10', agui_2, monto_agui)
ct.aguinaldo(bint, 'mant', agui_2, monto_agui)
ct.aguinaldo(bint, 'mant_10', agui_2, monto_agui)
ct.aguinaldo(bint, 'vig', agui_2, monto_agui)

# EsSalud

monto_tope=ct.tope(0.55, 4600)

ct.aporte_essalud(bint, 'cist', monto_cist, monto_tope)
ct.aporte_essalud(bint, 'cist_10', monto_cist, monto_tope)
ct.aporte_essalud(bint, 'psi', monto_psi, monto_tope)
ct.aporte_essalud(bint, 'psi_10', monto_psi, monto_tope)
ct.aporte_essalud(bint, 'mant', monto_mant, monto_tope)
ct.aporte_essalud(bint, 'mant_10', monto_mant, monto_tope)
ct.aporte_essalud(bint, 'vig', monto_vig, monto_tope)

ct.essalud(bint, 'cist', m_12)
ct.essalud(bint, 'cist_10', m_10)
ct.essalud(bint, 'psi', m_12)
ct.essalud(bint, 'psi_10', m_10)
ct.essalud(bint, 'mant', m_12)
ct.essalud(bint, 'mant_10', m_10)
ct.essalud(bint, 'vig', m_12)

# Generar totales

ct.total(bint, 'cas')
ct.total(bint, 'ess')
ct.total(bint, 'agui')
ct.total(bint, 'costo')

