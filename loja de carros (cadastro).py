# loja de carros (cadastro)
import customtkinter as ctk
from MySQLdb import *
from tkinter import*

host= '**coloque_o_host**'
user= '**coloque_o_usuario**'
password= '**coloque_a_senha**'
db= '**coloque_nome_da_base_de_dados**'
port= 'coloque_a_porta (sem aspas)'

global c
cnx= connect(host, user, password, db, port)
c= cnx.cursor(cursors.DictCursor)

menu= ctk.CTk()
width= menu.winfo_screenwidth()
height=menu.winfo_screenheight()
menu.attributes('-fullscreen',True)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme('green')

def insert(values, table, fields=None):
    global c
    global con
    query2= 'INSERT INTO '+ table
    if (fields):
         query2= query2 + ' (' + fields + ') '

    query2= query2 + ' VALUES' + ','.join(['('+ v +')' for v in values])

    print(query2)

    c.execute(query2)
    cnx.commit()

def select(fields, tables, where=None):
    global c
    query= 'SELECT ' + fields + ' FROM '+ tables
    if (where):
        query= query + ' WHERE ' + where

    c.execute(query)
    return c.fetchall()

def update(sets, table, where=None):
    global c, cnx
    query3= "UPDATE "+ table
    query3=query3+" SET "+",".join([field + " = '"+value+"'" for field,value in sets.items()])
    if (where):
        query3= query3 + " WHERE " + where

    print(query3)
    c.execute(query3)
    cnx.commit()

def sair():
    menu.destroy()

fr_menu= ctk.CTkFrame(menu, width=180, height=780, fg_color='light gray')
fr_menu.place(x=0,y=0)

btn_sair= ctk.CTkButton(fr_menu, text='x', width= 10, height=10, command=sair)
btn_sair.place(x=4,y=4)

result_lista_marca=[]
result_lista_marca2=[]
lista_modelo=[]
lista_ano=[]
lista_prp=[]

def marca(): 
    result_lista_marca.clear()
    result_lista_marca2.clear()
    lista_modelo.clear()
    lista_ano.clear()
    lista_prp.clear()

    fr_marca= ctk.CTkFrame(menu, width=1188, height=771)
    fr_marca.place(x=180, y=0)

    lb_marca= ctk.CTkLabel(fr_marca, text='Cadastro de Marca', font=('Arial', 35))
    lb_marca.place(x=364, y=45)

    ent_nome_marca= ctk.CTkEntry(fr_marca, placeholder_text='Nome da Marca', width=420, height=40)
    ent_nome_marca.place(x=314, y=140)

    fr_marca_cadastrados=ctk.CTkScrollableFrame(menu, width=420, height=450)
    fr_marca_cadastrados.place(x=480, y=230)

    lista_cadas1=[]
    cadas1=select('marca_nome','marca')
    for k in cadas1:
        for kk in k.values():
            lista_cadas1.append(kk)
    for kkk in lista_cadas1:
        fr_cadas1=ctk.CTkFrame(fr_marca_cadastrados, width=400, height=30, fg_color='gray')
        fr_cadas1.pack(pady=10)
        lb_cadas1= ctk.CTkLabel(fr_cadas1, text=kkk, font=('Arial', 15), text_color='black')
        lb_cadas1.place(x=5, y=5)

    # def cadastrados2():
    #     lista_cadas1=[]
    #     cadas1=select('marca_nome','marca')
    #     for k in cadas1:
    #         for kk in k.values():
    #             lista_cadas1.append(kk)
    #     for kkk in lista_cadas1:
    #         fr_cadas1=ctk.CTkFrame(fr_marca_cadastrados, width=400, height=30, fg_color='gray')
    #         fr_cadas1.pack(pady=10)
    #         lb_cadas1= ctk.CTkLabel(fr_cadas1, text=kkk, font=('Arial', 15), text_color='black')
    #         lb_cadas1.place(x=5, y=5)

    lista_de_verificacao= []                        
    def salvar_marca():
        marca_tem= select('*','marca')
        for p in marca_tem:
             for pp in p.values():
                lista_de_verificacao.append(pp)
        marca_result= ent_nome_marca.get()
        if marca_result in lista_de_verificacao:
            ent_nome_marca.configure(placeholder_text= 'Este item já esta cadastrado')
            btn_salvar_marca.focus()
        else:
            insert([f"'{marca_result}'"], 'marca', 'marca_nome')
        ent_nome_marca.delete(0,END)
        lista_cadas1.clear()

    btn_salvar_marca= ctk.CTkButton(fr_marca, text='Salvar', width=20, command=salvar_marca)
    btn_salvar_marca.place(x=494, y=190)

    def alterar():
        fr_alterar= ctk.CTkFrame(menu, width=1188, height=771)
        fr_alterar.place(x=180, y=0)
        def voltar():
            fr_alterar.destroy()
        btn_voltar=ctk.CTkButton(fr_alterar, text='<', width=10, height=10, command=voltar)
        btn_voltar.place(x=7,y=7)

        lb_alt= ctk.CTkLabel(fr_alterar, text='Alterar Marca', font=('Arial', 35))
        lb_alt.place(x=364, y=45)

        lista_alt=[]
        cadas1=select('marca_nome','marca')
        for i in cadas1:
            for ii in i.values():
                lista_alt.append(ii)
        opcoes_marca_alterar=ctk.CTkOptionMenu(fr_alterar, values=lista_alt, width=420, height=30)
        opcoes_marca_alterar.place(x=294, y=130)
        opcoes_marca_alterar.set('Valor para alterar')

        ent_marca_alt= ctk.CTkEntry(fr_alterar, width=420, placeholder_text='Novo Valor', height=30)
        ent_marca_alt.place(x=294, y=180)

        lista_id_alt=[]
        def salvar_alt():
            valor_alt=ent_marca_alt.get()
            valor_ant= opcoes_marca_alterar.get()
            valor_ant2= select('id_marca', 'marca', f"marca_nome = '{valor_ant}'")
            for v in valor_ant2:
                for vv in v.values():
                    lista_id_alt.insert(0,vv)
            alt_id2= lista_id_alt[0]
            update({'marca_nome':f'{valor_alt}'}, 'marca', f'id_marca={alt_id2}')
            ent_marca_alt.delete(0,END)
            opcoes_marca_alterar.set('Valor para alterar')

        btn_alt=ctk.CTkButton(fr_alterar, text='Salvar', command=salvar_alt)
        btn_alt.place(x=474, y=230)

    btn_alterar_marca=ctk.CTkButton(fr_marca, text='Alterar', width=20, command=alterar)
    btn_alterar_marca.place(y=700, x=494)

btn_marca= ctk.CTkButton(fr_menu, text='Cadastrar marca', width=140, height=40, command=marca)
btn_marca.place(x=20, y=84)

def modelo():
    result_lista_marca2.clear()
    lista_modelo.clear()
    lista_ano.clear()
    lista_prp.clear()

    pesquisa=select('marca_nome','marca')
    for i in pesquisa:
        for ii in i.values():
            result= result_lista_marca.append(ii)

    fr_modelo= ctk.CTkFrame(menu, width=1188, height=771)
    fr_modelo.place(x=180, y=0)

    lb_modelo= ctk.CTkLabel(fr_modelo, text='Cadastro de Modelo', font=('Arial', 35))
    lb_modelo.place(x=364, y=45)

    ent_nome_modelo= ctk.CTkEntry(fr_modelo, placeholder_text='Nome do Modelo', width=420, height=40)
    ent_nome_modelo.place(x=314, y=140)

    ent_origem_modelo= ctk.CTkEntry(fr_modelo, placeholder_text='País de origem', width=420, height=40)
    ent_origem_modelo.place(x=314, y=200)

    opcoes_marca= ctk.CTkOptionMenu(fr_modelo, values=result_lista_marca, width=420)
    opcoes_marca.place(x=314, y=260)
    opcoes_marca.set('Selecione uma marca')

    result_lista_id= []
    lista_modelo_tem=[]
    def salvar_modelo():
        result_nome_modelo= ent_nome_modelo.get()
        result_origem= ent_origem_modelo.get()
        result_opcoes_marca= opcoes_marca.get()
        modelo_tem= select('nome_modelo','modelo')
        for p in modelo_tem:
             for pp in p.values():
                lista_modelo_tem.append(pp)
        if result_nome_modelo in lista_modelo_tem:
            ent_nome_modelo.configure(placeholder_text= 'Este item já esta cadastrado')
            btn_salvar_modelo.focus()
        else:
            id= select('id_marca', 'marca', f"marca_nome = '{result_opcoes_marca}'")
            for v in id:
                for vv in v.values():
                    result_id= result_lista_id.append(vv)
            result_id2= result_lista_id[0]
            insert([f"DEFAULT, '{result_nome_modelo}', '{result_origem}', '{result_id2}'"], 'modelo')
        ent_nome_modelo.delete(0,END)
        ent_origem_modelo.delete(0,END)
        opcoes_marca.set('Selecione uma marca')

    btn_salvar_modelo= ctk.CTkButton(fr_modelo, text='Salvar', width=20, command=salvar_modelo)
    btn_salvar_modelo.place(x=494, y=300)

    fr_modelo_cadastrados=ctk.CTkScrollableFrame(menu, width=420, height=320)
    fr_modelo_cadastrados.place(x=480, y=350)

    lista_cadas2=[]
    cadas2=select('nome_modelo','modelo')
    for k in cadas2:
        for kk in k.values():
            lista_cadas2.append(kk)
    for kkk in lista_cadas2:
        fr_cadas2=ctk.CTkFrame(fr_modelo_cadastrados, width=400, height=30, fg_color='gray')
        fr_cadas2.pack(pady=10)
        lb_cadas2= ctk.CTkLabel(fr_cadas2, text=kkk, font=('Arial', 15), text_color='black')
        lb_cadas2.place(x=5, y=5)

    def alterar2():
        fr_modelo_alt= ctk.CTkFrame(menu, width=1188, height=771)
        fr_modelo_alt.place(x=180, y=0)

        def voltar_alt2():
            fr_modelo_alt.destroy()

        btn_volt_alt=ctk.CTkButton(fr_modelo_alt, text='<', command=voltar_alt2, height=10, width=10)
        btn_volt_alt.place(x=5,y=5)

        lb_modelo_alt= ctk.CTkLabel(fr_modelo_alt, text='Alterar Modelo', font=('Arial', 35))
        lb_modelo_alt.place(x=364, y=45)

        lista_alt2=[]
        cadas2=select('nome_modelo','modelo')
        for i in cadas2:
            for ii in i.values():
                lista_alt2.append(ii)
        opcoes_modelo_alt= ctk.CTkOptionMenu(fr_modelo_alt, width=420, values=lista_alt2)
        opcoes_modelo_alt.place(x=314, y=140)
        opcoes_modelo_alt.set('Valor para alterar')

        ent_nome_modelo_alt= ctk.CTkEntry(fr_modelo_alt, placeholder_text='Novo nome', width=420, height=40)
        ent_nome_modelo_alt.place(x=314, y=200)

        ent_origem_modelo_alt= ctk.CTkEntry(fr_modelo_alt, placeholder_text='Novo país de origem', width=420, height=40)
        ent_origem_modelo_alt.place(x=314, y=260)

        lista_alt3=[]
        cadas3=select('marca_nome','marca')
        for i in cadas3:
            for ii in i.values():
                lista_alt3.append(ii)
        opcoes_marca_alt= ctk.CTkOptionMenu(fr_modelo_alt, values=lista_alt3, width=420)
        opcoes_marca_alt.place(x=314, y=320)
        opcoes_marca_alt.set('Marca nova')

        def salvar_alt2():
            para_alterar= opcoes_modelo_alt.get()
            para_alterar2= select('id_modelo', 'modelo', f"nome_modelo='{para_alterar}'")
            for t in para_alterar2:
                for tt in t.values():
                    print(tt)
                    id_modelo_alterar= tt
            modelo_novo= ent_nome_modelo_alt.get()
            origem_novo= ent_origem_modelo_alt.get()
            marca_nova= opcoes_marca_alt.get()
            marca_nova2= select('id_marca', 'marca', f"marca_nome = '{marca_nova}'")
            for s in marca_nova2:
                for ss in s.values():
                    id_marca_nova= ss
            update({'nome_modelo': f'{modelo_novo}', 'origem': f'{origem_novo}', 'id_marca':f'{id_marca_nova}'}, 'modelo', f'id_modelo={id_modelo_alterar}')
            ent_nome_modelo_alt.delete(0,END)
            ent_origem_modelo_alt.delete(0,END)
            opcoes_modelo_alt.set('Valor para alterar')
            opcoes_marca_alt.set('Marca nova')

        btn_salvar_alt2=ctk.CTkButton(fr_modelo_alt, text='Salvar', command=salvar_alt2)
        btn_salvar_alt2.place(x=494, y=380)

    btn_cadas2=ctk.CTkButton(fr_modelo, text='Alterar', width=20, command=alterar2)
    btn_cadas2.place(x=494, y=700)

btn_modelo= ctk.CTkButton(fr_menu, text='Cadastrar modelo', width=140, height=40, command=modelo)
btn_modelo.place(x=20, y=194)

def ano():
    result_lista_marca.clear()
    result_lista_marca2.clear()
    lista_modelo.clear()
    lista_ano.clear()
    lista_prp.clear()

    fr_ano= ctk.CTkFrame(menu, width=1188, height=771)
    fr_ano.place(x=180, y=0)

    lb_ano= ctk.CTkLabel(fr_ano, text='Cadastro de Ano', font=('Arial', 35))
    lb_ano.place(x=374, y=45)

    ent_ano_fabricacao= ctk.CTkEntry(fr_ano, placeholder_text='Ano de fabricação', width=420, height=40)
    ent_ano_fabricacao.place(x=314, y=140)

    ent_ano_modelo= ctk.CTkEntry(fr_ano, placeholder_text='Ano do modelo', width=420, height=40)
    ent_ano_modelo.place(x=314, y=200)

    def salvar_ano():
        ano_fab_result= ent_ano_fabricacao.get()
        ano_modelo_result= ent_ano_modelo.get()
        insert([f"DEFAULT, '{ano_fab_result}', '{ano_modelo_result}'"], 'ano')
        ent_ano_modelo.delete(0,END)
        ent_ano_fabricacao.delete(0,END)

    btn_salvar_ano= ctk.CTkButton(fr_ano, text='Salvar', width=20, command=salvar_ano)
    btn_salvar_ano.place(x=494, y=250)

btn_ano= ctk.CTkButton(fr_menu, text='Cadastrar ano', width=140, height=40, command=ano)
btn_ano.place(x=20, y=304)

def proprietario():
    result_lista_marca.clear()
    result_lista_marca2.clear()
    lista_modelo.clear()
    lista_ano.clear()
    lista_prp.clear()

    fr_proprietario= ctk.CTkFrame(menu, width=1188, height=771)
    fr_proprietario.place(x=180, y=0)

    lb_proprietario= ctk.CTkLabel(fr_proprietario, text='Cadastro de Proprietario', font=('Arial', 35))
    lb_proprietario.place(x=344, y=45)

    ent_nome_prp= ctk.CTkEntry(fr_proprietario, placeholder_text='Nome do proprietário', width=420, height=40)
    ent_nome_prp.place(x=314, y=140)

    ent_cpf_prp= ctk.CTkEntry(fr_proprietario, placeholder_text='CPF', width=420, height=40)
    ent_cpf_prp.place(x=314, y=200)

    ent_celular_prp= ctk.CTkEntry(fr_proprietario, placeholder_text='Numero de telefone', width=420, height=40)
    ent_celular_prp.place(x=314, y=260)
    
    def salvar_prp():
        result_nome= ent_nome_prp.get()
        result_cpf= ent_cpf_prp.get()
        result_celular= ent_celular_prp.get()
        insert([f"DEFAULT, '{result_nome}', '{result_cpf}', '{result_celular}'"], 'proprietario')
        ent_celular_prp.delete(0,END)
        ent_cpf_prp.delete(0,END)
        ent_nome_prp.delete(0,END)

    btn_salvar_prp= ctk.CTkButton(fr_proprietario, text='Salvar', width=20, command=salvar_prp)
    btn_salvar_prp.place(x=494, y=320)

btn_proprietario= ctk.CTkButton(fr_menu, text='Cadastrar proprietário', width=140, height=40, command=proprietario)
btn_proprietario.place(x=20, y=414)

def veiculo():
    result_lista_marca.clear()

    fr_veiculo= ctk.CTkFrame(menu, width=1188, height=771)
    fr_veiculo.place(x=180, y=0)

    lb_veiculo= ctk.CTkLabel(fr_veiculo, text='Cadastro de Veículo', font=('Arial', 35))
    lb_veiculo.place(x=344, y=45)

    def verificar(q):
        lista_modelo.clear()
        r_marca1= opcoes_marca.get()
        r_marca_id=select('id_marca', 'marca', f"marca_nome = '{r_marca1}'")
        for i in r_marca_id:
            for ii in i.values():
                lista_id_marca.insert(0, ii)
        r_marca2=lista_id_marca[0]
        pesquisa2=select('nome_modelo','modelo',f'id_marca={r_marca2}')
        for a in pesquisa2:
            for aa in a.values():
                lista_modelo.append(aa)
        opcoes_modelo.configure(values=lista_modelo)
    pesquisa=select('marca_nome','marca')
    for i in pesquisa:
        for ii in i.values():
            result= result_lista_marca2.append(ii)
    opcoes_marca= ctk.CTkOptionMenu(fr_veiculo, values=result_lista_marca2, width=420, command=verificar)
    opcoes_marca.place(x=314, y=140)
    opcoes_marca.set('Selecione uma marca')
    btn_mais_marca=ctk.CTkButton(fr_veiculo, text='...', width=10, command=marca)
    btn_mais_marca.place(x=740, y=140)

    opcoes_modelo= ctk.CTkOptionMenu(fr_veiculo, width=420)
    opcoes_modelo.place(x=314, y=200)
    opcoes_modelo.set('Selecione um modelo')
    btn_mais_modelo=ctk.CTkButton(fr_veiculo, text='...', width=10, command=modelo)
    btn_mais_modelo.place(x=740, y=200)

    pesquisa3=select('ano_fabricaco','ano')
    for b in pesquisa3:
        for bb in b.values():
            lista_ano.append(bb)
    opcoes_ano= ctk.CTkOptionMenu(fr_veiculo, values=lista_ano, width=420)
    opcoes_ano.place(x=314, y=260)
    opcoes_ano.set('Selecione um ano')
    btn_mais_ano=ctk.CTkButton(fr_veiculo, text='...', width=10, command=ano)
    btn_mais_ano.place(x=740, y=260)

    pesquisa4=select('nome_proprietario','proprietario')
    for c in pesquisa4:
        for cc in c.values():
            lista_prp.append(cc)
    opcoes_proprietario= ctk.CTkOptionMenu(fr_veiculo, values=lista_prp, width=420)
    opcoes_proprietario.place(x=314, y=320)
    opcoes_proprietario.set('Selecione um proprietário')
    btn_mais_prp=ctk.CTkButton(fr_veiculo, text='...', width=10, command=proprietario)
    btn_mais_prp.place(x=740, y=320)

    ent_cor= ctk.CTkEntry(fr_veiculo, placeholder_text='Cor', width=420, height=40)
    ent_cor.place(x=314, y=380)

    ent_placa= ctk.CTkEntry(fr_veiculo, placeholder_text='Placa', width=420, height=40)
    ent_placa.place(x=314, y=440)

    ent_valor= ctk.CTkEntry(fr_veiculo, placeholder_text='Valor *', width=420, height=40)
    ent_valor.place(x=314, y=500)

    ent_fipe= ctk.CTkEntry(fr_veiculo, placeholder_text='Valor fipe', width=420, height=40)
    ent_fipe.place(x=314, y=560)

    ent_km= ctk.CTkEntry(fr_veiculo, placeholder_text='Km *', width=420, height=40)
    ent_km.place(x=314, y=620)

    lista_id_modelo=[]
    lista_id_marca=[]
    lista_id_ano=[]
    lista_id_prp=[]
    def salvar_veiculo():
        r_marca1= opcoes_marca.get()
        r_marca_id=select('id_marca', 'marca', f"marca_nome = '{r_marca1}'")
        for d in r_marca_id:
            for dd in d.values():
                lista_id_marca.insert(0,dd)
        r_marca2=lista_id_marca[0]
        print(r_marca2)
        
        r_modelo= opcoes_modelo.get()
        r_modelo_id=select('id_modelo', 'modelo', f"nome_modelo = '{r_modelo}'")
        for e in r_modelo_id:
            for ee in e.values():
                lista_id_modelo.insert(0,ee)
        r_modelo2=lista_id_modelo[0]
        print(r_modelo2)
        # lista_id_modelo.clear()

        r_ano= opcoes_ano.get()
        r_ano_id=select('id_ano', 'ano', f"ano_fabricaco = '{r_ano}'")
        for f in r_ano_id:
            for ff in f.values():
                lista_id_ano.insert(0,ff)
        r_ano2=lista_id_ano[0]
        print(r_ano2)

        r_prp= opcoes_proprietario.get()
        r_prp_id=select('id_proprietario', 'proprietario', f"nome_proprietario = '{r_prp}'")
        for g in r_prp_id:
            for gg in g.values():
                lista_id_prp.insert(0,gg)
        r_prp2=lista_id_prp[0]
        print(r_prp2)

        cor= ent_cor.get()
        placa= ent_placa.get()
        valor= ent_valor.get()
        fipe= ent_fipe.get()
        km= ent_km.get()

        insert([f"DEFAULT, '{r_marca2}', '{r_modelo2}', '{r_ano2}', '{r_prp2}', '{cor}', '{placa}', {valor}, {fipe}, {km}"], 'veiculo')        

    btn_salvar_veiculo= ctk.CTkButton(fr_veiculo, text='Salvar', width=20, command=salvar_veiculo)
    btn_salvar_veiculo.place(x=494, y=680)

btn_veiculo= ctk.CTkButton(fr_menu, text='Cadastrar veiculo', width=140, height=40, command=veiculo)
btn_veiculo.place(x=20, y=524)

# def pesquisa():
#     fr_pesquisa= ctk.CTkFrame(menu, width=1188, height=771)
#     fr_pesquisa.place(x=180, y=0)

#     lb_pesquisa= ctk.CTkLabel(fr_pesquisa, text='Pesquisa de veiculos', font=('Arial', 35))
#     lb_pesquisa.place(x=344, y=45)

#     # fr_pesquisados=ctk.CTkScrollableFrame(menu, width=420, height=520)
#     # fr_pesquisados.place(x=480, y=200)

#     def pesquisar():
#         item= ent_pesquisa.get()
#         pesquisa_select_modelo= select('id_modelo', 'modelo', f"nome_modelo= '{item}'")
#         for x in pesquisa_select_modelo:
#             for xx in x.values():
#                 pesquisa_select_modelo=xx
#         pesquisa_select_marca= select('id_marca', 'marca', f"marca_nome= '{item}'")
#         for z in pesquisa_select_marca:
#             for zz in z.values():
#                 pesquisa_select_marca=zz

#         result_pesquisa_modelo= select('id_veiculo', 'veiculo', f"id_modelo='{pesquisa_select_modelo}'")
#         result_pesquisa_marca= select('id_veiculo', 'veiculo', f"id_marca='{pesquisa_select_marca}'")
#         result_pesquisa_marca2=[]
#         for j in result_pesquisa_marca:
#             for jj in j.values():
#                 result_pesquisa_marca2.insert(0,jj)
#         result_pesquisa_marca2=result_pesquisa_marca2[0]

#         result= select('cor', 'veiculo', f"id_veiculo= '{result_pesquisa_marca2}'")
#         print(result)
#         teste= {'nome':['Daniel'], 'idade':['13'],}
#         df_dicionario=pd.DataFrame(teste)
#         df_dicionario.tail()

#     ent_pesquisa= ctk.CTkEntry(fr_pesquisa, placeholder_text='Pesquise um modelo ou marca', width=420, height=40)
#     ent_pesquisa.place(x=314, y=140)

#     btntest= ctk.CTkButton(fr_pesquisa, text='teste', command=pesquisar)
#     btntest.place(x=180, y=140)

btn_pesquisa=ctk.CTkButton(fr_menu, text='Pesquisar', width=140, height=40)
btn_pesquisa.place(x=20, y=634)

menu.mainloop()