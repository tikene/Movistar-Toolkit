# Movistar Exploit Toolkit


**Incluye dos scripts probados en la última versión (2021) de los routers Movistar**

  ![movrou](https://user-images.githubusercontent.com/92279236/138614508-9f34fbf0-2649-4d2e-87ed-768bc7f6b929.png)
  

Ambos scripts bypasean el limite de intentos de inicio de sesion implementado (pobremente) por Movistar para evitar este tipo de ataques 

![loglimit](https://user-images.githubusercontent.com/92279236/138266890-609b1203-1ef8-4255-b5a0-f63864a42b08.png)

 

  **Opcion 1** -> Realiza un ataque DOS en la red Movistar local mediante el envío continuo de inicios de sesión. 

  **Opcion 2** -> Realiza un ataque de tipo diccionario, probando las contraseñas de la lista que selecciones (edita el script para cambiar los threads y la wordlist)

![movt1](https://user-images.githubusercontent.com/92279236/138661946-c506567b-3f67-44ee-a215-e10547f3b874.png)
![movt2](https://user-images.githubusercontent.com/92279236/138661959-717e3ed1-726b-419f-98eb-0aef8537e486.png)

Requieren acceso al panel de configuración WiFi y, por lo tanto, estar conectado a la red. En caso de que la puerta de enlace predeterminada no sea 192.168.1.1, puedes cambiarla editando movistar_dos.py
