# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:54:33 2026
"""
# DESENVOLVER UMA APLICACAO DE SOFTWARE TIPO CRUD
#DE TAL FORMA A CADASTRAR, CONSULTAR, DELETAR,
#LISTAR e ALTERAR DADOS DE UMA LISTA DE LISTAS.
#
#TEMA: AGENDA DE CONTATOS
#
#CAMPOS: NOME, SEXO, CELULAR, EMAIL, IDADE
#
#DESENVOLVER UM MENU DE OPCOES.
#
#SOFTWARE TABAJARA - AGENDA TABAJARA
#
# 1 - CADASTRAR
# 2 - CONSULTAR
# 3 - LISTAR
# 4 - ALTERAR
# 5 - DELETAR
# 0 - SAIR
#
# QUAL A SUA OPCAO: 
#
#
dados=[ 
       ["ADAMASTHOR","M","19 912345678","adm@gmail.com",18],
       ["MARISMENIA","F","19 956776564","mari@gmail.com",76],
       ["ONLAYNY","F","19 934786523","onlayny@gmail.com",22],
       ["OFFYLAYNY","F","19 945123278","offylayny@gmail.com",35],
       ["HORKUTYZ","M","19 990091237","hkt@gmail.com",27]
       ]

opcao=""

while(opcao!="0"):
    print("\nAGENDA TABAJARA\n")
    print(" 1 - CADASTRAR")
    print(" 2 - CONSULTAR")
    print(" 3 - LISTAR")
    print(" 4 - ALTERAR")
    print(" 5 - DELETAR")
    print(" 0 - SAIR")
    print("")
    opcao=input("QUAL A SUA OPCAO: ")
    
    if(opcao=="1"):
        print("\n***** CADASTRAR *****")

            
    elif(opcao=="2"):
        print("\n***** CONSULTAR *****")
 
        
    elif(opcao=="3"):
        print("\n***** LISTAR *****")
        
    elif(opcao=="4"):
        print("\n***** ALTERAR *****")

    elif(opcao=="5"):
        print("\n***** DELETAR *****")



        
