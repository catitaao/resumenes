


pizza_favorita_cliente, consulta_anidada




def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
        pedidos_cliente = set(map(lambda pedido: pedido.id_pedido, 
        filter(lambda pedido: 
        pedido.id_cliente == id_cliente, generador_pedidos)))
        contador_pizzas = defaultdict(int)
        pedidos_filtrados = map(lambda pedido: (pedido.nombre.split("_")[0], pedido.cantidad), 
        filter(lambda pedido: pedido.id_pedido in pedidos_cliente))
        
        pizzas_contadas = reduce(pedidos_filtrados[0], pedidos_filtrados[1], defaultdict(int))
        cant_max = max(contador_pizzas.values())
        return list(filter(lambda item: item[1] == cant_max, pizzas_contadas.items()))



def consulta_anidada(instrucciones: dict) -> Any:
    opciones_funciones = {
    "cargar_pizzas": cargar_pizzas,
    "cargar_locales": cargar_locales,
    "cargar_pedidos": cargar_pedidos,
    "cargar_contenido_pedidos": cargar_contenido_pedidos,
    "cliente_indeciso": cliente_indeciso,
    "pizzas_con_ingrediente": pizzas_con_ingrediente,
    "pizzas_pagables_de_un_tamano": pizzas_pagables_de_un_tamano,
    "cantidad_empleados_pais": cantidad_empleados_pais,
    "total_ahorrado_pedidos": total_ahorrado_pedidos}
    funcion = opciones_funciones.get(instrucciones.get("funcion"))
    analisis_instrucciones = {
        key: consulta_anidada(value)
        if isinstance(value, dict) and "funcion" in value else value
        for key, value in instrucciones.items() if key != "funcion"}
    return funcion(**analisis_instrucciones)



def consulta_anidada(instrucciones: dict) -> Any:
    def ejecutar(dic):
        if isinstance(dic, dict):
            funcion = dic.get('funcion')
            args = {k: ejecutar(v) if isinstance(v, dict) else v for k, v in dic.items() if k != 'funcion'}
            return globals()[funcion](**args)
        return dic
    return ejecutar(instrucciones)




def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
        pedidos_cliente = filter(lambda pedido: pedido.id_cliente == id_cliente, 
                                 generador_pedidos)
        id_pedidos = {pedido.id_pedido for pedido in pedidos_cliente}
        pizzas_pedidas = filter(lambda cont: cont.id_pedido in id_pedidos, 
                                generador_contenido_pedidos)
        contador_pizzas = Counter(map(lambda contenido: 
                                      "_".join(contenido.nombre.split("_")[:-1]), 
                                      pizzas_pedidas))
        pizza_fav = reduce(lambda pizza_a, pizza_b: pizza_a if pizza_a[1] > pizza_b[1] 
                           else pizza_b, contador_pizzas.items(), ("", 0))
        if pizza_fav[1] > 0:
            return [(pizza_fav[0], pizza_fav[1])]
        return iter()


def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
    pedidos_cliente = filter(lambda pedido: pedido.id_cliente == id_cliente, generador_pedidos)
    pizzas = (contenido.nombre.split("_")[0]
              for pedido in pedidos_cliente 
              for contenido in generador_contenido_pedidos 
              if contenido.id_pedido == pedido.id_pedido)
    contador_pizzas = Counter(pizzas)
    if not contador_pizzas:
        return []
    pizza_fav, cantidad = contador_pizzas.most_common(1)[0]
    return [(pizza_fav, cantidad)]



    dict_pedidos = {
        cont.id_pedido: cont.nombre.split("_")[0]
        for cont in generador_contenido_pedidos
    }
    pizzas = [
        dict_pedidos[cont.id_pedido]
        for pedido in generador_pedidos
        if pedido.id_cliente == id_cliente
        for cont in generador_contenido_pedidos
        if cont.id_pedido in dict_pedidos and cont.id_pedido == pedido.id_pedido
    ]
    contador_pizzas = Counter(pizzas)
    if not contador_pizzas:
        return[]
    pizza_fav, cant = contador_pizzas.most_common(1)[0]
    return [(pizza_fav, cant)]



def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
    lista_pedidos = list(generador_pedidos)
    lista_contenido_pedidos = list(generador_contenido_pedidos)

    # Crear un diccionario de contenido de pedidos por id de pedido
    dict_pedidos = {}
    for cont in lista_contenido_pedidos:
        if cont.id_pedido not in dict_pedidos:
            dict_pedidos[cont.id_pedido] = []
        dict_pedidos[cont.id_pedido].append(cont.nombre.split("_")[0])
    
    # Crear una lista de nombres de pizzas basadas en los pedidos del cliente
    pizzas = [
        pizza
        for pedido in lista_pedidos
        if pedido.id_cliente == id_cliente
        for pizza in dict_pedidos.get(pedido.id_pedido, [])
    ]
    
    # Contar la cantidad de cada pizza
    contador_pizzas = Counter(pizzas)
    
    if not contador_pizzas:
        return []
    
    # Obtener la pizza más pedida y su cantidad
    pizza_fav, cant = contador_pizzas.most_common(1)[0]
    
    return [(pizza_fav, cant)]



def consulta_anidada(instrucciones: dict) -> Any:
    def ejecutar(dic):
        if isinstance(dic, dict):
            # Obtener la función que se va a ejecutar
            funcion = dic.get('funcion')
            # Preparar los argumentos de la función
            args = {k: ejecutar(v) if isinstance(v, dict) else v for k, v in dic.items() if k != 'funcion'}
            # Ejecutar la función solicitada con los argumentos preparados
            return globals()[funcion](**args)
        return dic
    return ejecutar(instrucciones)





#error usa total_ahorrado_pedidos, cliente_indeciso

#python3 -m unittest -v -b tests_publicos.test_consulta_anidada
###falla 1 test...