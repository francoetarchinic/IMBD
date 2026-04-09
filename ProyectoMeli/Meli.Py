## 1

import requests
from lxml import html
'''para cada página:
    obtener html
    obtener lista de productos
    para cada producto:
        extraer campos
        guardar
'''

cookies = {
    '_csrf': 'RMFvfHfWOfwZp25TXSYRoZ6B',
    '_mldataSessionId': 'c68a5a02-ad0c-4604-90c2-e626d3086fce',
    'cp': '1048',
    'inferredZipcode': 'true',
    'c_ui-navigation': '6.8.0',
    'g_state': '{"i_l":0,"i_ll":1769187666331,"i_b":"7OmlyIjqzW0vu5fWO+5787QolLbiDl+mcws/zgS8PUk","i_e":{"enable_itp_optimization":0}}',
    '_hjSessionUser_720735': 'eyJpZCI6ImZlYmVjYzNhLThlMTQtNWMyOC05ZGEyLWNhNGU4MzUyYjJjZiIsImNyZWF0ZWQiOjE3NjkxODc2NjY0NDYsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjSession_720735': 'eyJpZCI6IjEyN2M5MmUzLTZlZWUtNDRlMi05N2IyLWZhMDkzOTgxM2MwOSIsImMiOjE3NjkxODc2NjY0NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_d2id': '134068cd-3fdf-4d9f-a3a5-c6496d19998a',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.mercadolibre.com.ar/ofertas?container_id=MLA916439-1',
    'rtt': '50',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'viewport-width': '807',
    # 'cookie': '_csrf=RMFvfHfWOfwZp25TXSYRoZ6B; _mldataSessionId=c68a5a02-ad0c-4604-90c2-e626d3086fce; cp=1048; inferredZipcode=true; c_ui-navigation=6.8.0; g_state={"i_l":0,"i_ll":1769187666331,"i_b":"7OmlyIjqzW0vu5fWO+5787QolLbiDl+mcws/zgS8PUk","i_e":{"enable_itp_optimization":0}}; _hjSessionUser_720735=eyJpZCI6ImZlYmVjYzNhLThlMTQtNWMyOC05ZGEyLWNhNGU4MzUyYjJjZiIsImNyZWF0ZWQiOjE3NjkxODc2NjY0NDYsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_720735=eyJpZCI6IjEyN2M5MmUzLTZlZWUtNDRlMi05N2IyLWZhMDkzOTgxM2MwOSIsImMiOjE3NjkxODc2NjY0NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _d2id=134068cd-3fdf-4d9f-a3a5-c6496d19998a',
}

for page in range(1, 11):
   

    params = {
        'container_id': 'MLA916439-1',
        'page': page}
    try:
        response = requests.get('https://www.mercadolibre.com.ar/ofertas', params=params, headers=headers)
               
        tree = html.fromstring(response.text)  
        
        full_products = tree.xpath('//div[@class="items-with-smart-groups"]/div')
        for product in full_products:
            #Nombre del producto
            try:
                name = product.xpath('.//h3[contains(@class,"poly-component__title-wrapper")]/a')[0].text
                print(name)
            except Exception as e:
                name = ""
                print ("Un error al obtener el nombre", e)
                
            #Link del producto
            try:
                link = product.xpath('.//h3[contains(@class,"poly-component__title-wrapper")]/a/@href')[0]
                print(link)
            except Exception as e:
                link = ""
                print ("Un error al obtener el link",e)
            
            #Nombre del vendedor
            try:
                vendedor = product.xpath('.//span[contains(@class,"poly-component__seller")]')[0].text
                vendedor = vendedor.replace("Por ","").strip()
                print(vendedor)
            except Exception as e:
                vendedor = ""
                print ("Un error al obtener el vendedor",e)
                
            #Precio anterior
            try:
                precio_anterior = product.xpath('.')[0].text
                precio_anterior = precio_anterior.replace("$ ","").strip()
                print(precio_anterior)
            except Exception as e:
                precio_anterior = "" 
                print ("Un error al obtener el vendedor",e)
            
        
        

            
        
            product_dic = {
                "name": name,
                "url": link,
                "vendedor": vendedor,
                
                
                
            }
            
            print("Esto se va a guardar:", product_dic)
            
            break    
                
           
            
          
                 
        
        
        break 
    ## esto se borra para poder cortar la ejecucion del for
    except Exception as e:
        print ("Error:", e)
