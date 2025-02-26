### Definiciones de TSP y VRP.
**(Problema del Viajante, TSP)**: Se da un grafo completo $G=(V,E)$ con $n=|V|$ vértices (también llamados ciudades) y una función de costo (o distancia) $c: V\times V \to \mathbb{R}{\ge 0}$ que asigna a cada par de ciudades un costo no negativo de viaje. El Problema del Viajante busca un ciclo Hamiltoniano de costo mínimo en $G$. Formalmente, en su versión de decisión, una instancia de TSP es una terna $(G,c,B)$ donde $B\in \mathbb{R}{>0}$ es una cota de costo, y la pregunta es si existe un ciclo Hamiltoniano $v_{1}\to v_{2}\to \cdots \to v_{n}\to v_{1}$ (donde ${v_1,\ldots,v_n}=V$ y todos los $v_i$ son distintos) tal que la suma de costos de sus aristas sea a lo sumo $B$​. Es decir, ¿existe una permutación $p$ de ${1,\dots,n}$ con $v_{p(1)}=v_{1}$ fija, tal que
\[
\begin{aligned}
    &c(v_{p(1)}, v_{p(2)}) + c(v_{p(2)}, v_{p(3)}) + \dots \\
    &+ c(v_{p(n-1)}, v_{p(n)}) + c(v_{p(n)}, v_{p(1)}) \leq B?
\end{aligned}
\]

Si la respuesta es sí, decimos que la instancia es aceptada (existe un tour de costo $\le B$); en caso contrario, la instancia es rechazada. (Nótese que el TSP así definido es un problema de decisión NP-completo​, equivalente a preguntar si el peso de la solución óptima del TSP es $\le B$.)

**(Problema de Ruteo de Vehículos, VRP)**: Sea $G'=(V',E')$ un grafo completo con un vértice distinguido $d\in V'$ llamado depósito (o base) y un conjunto de $m$ vehículos idénticos disponibles. Cada vértice $v\in V'\setminus{d}$ representa un cliente que debe ser visitado exactamente una vez. Se da una función de costo $c':V'\times V' \to \mathbb{R}{\ge 0}$ que da la distancia o costo de viajar entre cualquier par de ubicaciones (depósito o clientes). 

Adicionalmente, cada cliente $v$ puede tener una demanda $q(v)\in \mathbb{Z}{\ge 0}$ de cierta capacidad, y cada vehículo tiene una capacidad máxima $Q$ de demanda que puede atender (en la variante VRP capacitado, CVRP). En el Problema de Ruteo de Vehículos, se pregunta si es posible encontrar hasta $m$ rutas (recorridos) de los vehículos, todas comenzando y terminando en el depósito $d$, que cumplan:
 
**a** cobertura – cada cliente $v\in V'\setminus{d}$ es visitado por exactamente uno de los recorridos; 
**b** capacidades – la suma de demandas $q(v)$ de los clientes atendidos en la ruta de cada vehículo no excede la capacidad $Q$ de ese vehículo (si se incluye la restricción de capacidad);
**c** costo total – la suma de los costos de viaje de todas las rutas no excede un valor dado $B$. 

En la versión de decisión, una instancia de VRP es una 6-tupla $(G',c',d,m,Q,B)$ (suponiendo demandas $q(v)$ integradas en $G'$ o en $c'$), y la pregunta es si existe un conjunto de a lo sumo $m$ rutas válidas que cubran todos los clientes cumpliendo **a – c** dentro del costo total $B$. Una solución que satisface estas condiciones afirmativamente se denomina ruteo válido de costo $\le B$. Si además $m$ es exactamente el número de rutas usadas, normalmente buscamos $m$ mínimo o predefinido; aquí tomamos $m$ como un parámetro de la instancia que limita la cantidad de vehículos disponibles. (Obsérvese que si $m=1$ y no hay restricciones de capacidad, VRP se reduce a encontrar una sola ruta que visite a todos los clientes y regrese al depósito, lo que equivale a un ciclo Hamiltoniano mínimo en $G'$ – en efecto, el TSP es un caso especial de VRP​.

### Reducción de TSP a VRP.
Dada una instancia $(G=(V,E),c,B)$ del Problema del Viajante (TSP-decisión), construiremos en tiempo polinomial una instancia equivalente $(G',c',d,m,Q,B')$ del Problema de Ruteo de Vehículos (VRP-decisión). La idea central es que el VRP generaliza al TSP cuando restringimos a $m=1$ vehículo y hacemos trivial la restricción de capacidad. En consecuencia, cualquier instancia de TSP puede transformarse en una instancia de VRP que “simule” el mismo recorrido con un solo vehículo. La construcción es la siguiente:

**Paso 1 (Grafo y depósito)**: Sea $G=(V,E)$ el grafo completo de la instancia TSP original. Definimos el grafo $G'=(V',E')$ para la instancia VRP de salida de la siguiente forma: tomamos $V'=V$ (es decir, los mismos vértices que en $G$) y $E'=E$ con la misma estructura de grafo completo. Elegimos un vértice arbitrario de $V$ para actuar como depósito $d$. Por conveniencia, podemos tomar $d$ como, por ejemplo, el vértice $v_1$ (la “ciudad 1”) de $V$. En adelante, en $G'$, el vértice $d$ es el depósito, y el conjunto de clientes a ser atendidos será $V'\setminus{d}=V\setminus{d}$ (todos los demás vértices).

**Paso 2 (Costos)**: Definimos la función de costos $c':V'\times V'\to \mathbb{R}_{\ge 0}$ de la instancia VRP exactamente igual que $c$ en la instancia TSP original para cada par de vértices. Es decir, para cualquier par $u,v\in V'$, se define $c'(u,v)=c(u,v)$. De este modo, las distancias (o costos de viaje) entre ciudades en la instancia VRP coinciden exactamente con las de la instancia TSP dada.

**Paso 3 (Vehículos y capacidad)**: Definimos el número de vehículos $m=1$. Solo se permite usar un vehículo en la solución VRP. Este vehículo tendrá capacidad $Q$ suficientemente grande para atender a todos los clientes. Por ejemplo, si cada cliente se considera con demanda $q(v)=1$, podemos fijar $Q=|V'\setminus{d}| = n-1$, de forma que el único vehículo pueda visitar a todos los clientes sin violar la restricción de capacidad (en caso de que estemos considerando VRP capacitado). Si la variante de VRP no incluye demandas/capacidades, podemos omitir este paso; en esencia estamos eliminando cualquier limitante de capacidad para que no restrinja la ruta. Lo importante es que un único vehículo pueda cubrir todo el conjunto de clientes en una sola ruta.

**Paso 4 (Umbral de costo)**: Sea $B$ el umbral de costo de la instancia TSP. Tomamos el mismo valor $B$ como umbral de costo total permitido $B'$ en la instancia VRP. Dado que pretendemos que una ruta del vehículo en VRP replique el tour del viajante, debe cumplirse la misma cota de costo. (Si por la construcción hubiera alguna ligera modificación en costos, la ajustaríamos; pero en nuestra transformación $c'=c$, así que usamos el mismo $B$).

Tras estos pasos, la instancia resultante de VRP es $I' = (G'=(V',E'),c',d,m=1,Q,B' = B)$. Esta construcción es claramente computable en tiempo polinomial respecto del tamaño de $G$: básicamente consiste en copiar el grafo y añadir constantes $m$ y $Q$. El tamaño de la descripción de $I'$ es $O(|V|^2)$ debido a la matriz de costos, de la misma orden que la instancia original, por lo que la transformación es eficiente (polinómica).

### Corrección de la reducción.
Debemos demostrar que la instancia construida $I'$ de VRP es sí exactamente cuando la instancia original $I$ de TSP es sí. En otras palabras, probaremos que existe un tour Hamiltoniano en $G$ de costo $\le B$ si y solo si existe una solución de ruteo de vehículos en $G'$ (con $m=1$ vehículo) de costo $\le B$. Establecemos las dos direcciones de la equivalencia:

**(Si)** Supongamos que la instancia TSP $(G,c,B)$ es satisfactoria, es decir, existe un ciclo Hamiltoniano en $G$ cuyo costo total no excede $B$. 
Llamemos $v_{1}\to v_{2}\to \dots \to v_{n}\to v_{1}$ a dicho ciclo (con $v_1$ como ciudad inicial, sin pérdida de generalidad podemos elegir como inicio el vértice $v_1$ que designamos depósito). 

Como este ciclo visita cada vértice de $V$ exactamente una vez y retorna al inicial $v_1$, podemos interpretarlo directamente como una ruta válida para un solo vehículo en la instancia VRP. 

En efecto, consideremos la ruta que parte del depósito $d=v_1$, visita en el orden dado los clientes $v_2, v_3, \dots, v_n$ y regresa al depósito $v_1$. Esta ruta en $G'$ utiliza un solo vehículo, comienza y termina en $d$, y cubre todos los clientes $V'\setminus{d} = {v_2,\dots,v_n}$. 

Por construcción, los costos $c'$ son iguales a $c$, así que el costo total de esta ruta es exactamente la suma de los costos $c(v_1,v_2)+c(v_2,v_3)+\cdots+c(v_n,v_1)$, que por hipótesis es $\le B$. Además, la capacidad del vehículo no se viola porque ajustamos $Q$ para que soporte hasta $n-1$ clientes. 

Por lo tanto, esta ruta constituye una solución factible para la instancia VRP con costo $\le B$. Así hemos construido, a partir del ciclo Hamiltoniano del TSP, una solución de VRP que demuestra que $I'$ es instancia aceptada.

**(Solo si)** Ahora supongamos que la instancia VRP $I'=(G',c',d,m=1,Q,B)$ construida es satisfactoria, es decir, existe al menos una solución de ruteo (un conjunto de rutas) con costo total $\le B$. Dado que $m=1$, solo se permite una ruta; llamemos $R$ a esa ruta. $R$ debe iniciar en el depósito $d$ y terminar en $d$, visitando a cada cliente de $V'\setminus{d}$ exactamente una vez, porque en VRP cada cliente debe ser cubierto. 
Sea la secuencia de vértices visitados en $R$:
\[
R: d = u_0 \to u_1 \to u_2 \to \dots \to u_k \to u_{k+1} = d
\]

donde ${u_1,\dots,u_k} = V'\setminus{d}$. Es decir, $R$ parte de $d$, recorre todos los clientes $u_1,\ldots,u_k$ (sin repeticiones) y regresa a $d$. 

Dado que $V' = V$ y $d\in V$, observamos que ${d, u_1,\ldots,u_k} = V$. En efecto, $R$ ha visitado a todos los vértices originales: $d$ (al inicio/final) y todos los demás $u_i$. Por lo tanto, si ignoramos el hecho de que $d$ aparece repetido al comienzo y final, la secuencia $d, u_1, \ldots, u_k, d$ constituye un ciclo que pasa por cada vértice de $V$ exactamente una vez (volviendo al inicio). En otras palabras, $(d, u_1, u_2, \ldots, u_k)$ es un ciclo Hamiltoniano en el grafo original $G$. Además, el costo total de esa ruta $R$ según $c'$ es a lo sumo $B$ (por hipótesis de que $R$ es solución de VRP $\le B$). Pero $c'$ coincide con $c$, luego el costo de dicho ciclo en $G$ bajo $c$ es $\le B$. Así hemos obtenido un ciclo Hamiltoniano en $G$ de costo $\le B$. 
Concluimos que la instancia TSP original es respondida afirmativamente.

Hemos demostrado entonces que, partiendo de un tour del viajante válido obtenemos una ruta de vehículos válida, y viceversa, cualquier ruta de VRP con un vehículo corresponde a un ciclo Hamiltoniano del TSP original, conservando el costo. Esta correspondencia es biyectiva: cada solución factible de TSP induce una solución factible de VRP de igual costo, y viceversa. Por lo tanto, la construcción dada reduce correctamente TSP a VRP, en el sentido de que $(G,c,B)$ es instancia sí de TSP si y solo si $(G',c',d,1,Q,B)$ es instancia sí de VRP.

### Complejidad computacional.
La transformación descrita es claramente polinomial en el tamaño de la entrada. Si $n=|V|$, describir $G'$ toma $O(n)$ para los vértices y $O(n^2)$ para listar todos los costos (similar al input original); añadir el depósito $d$, el número de vehículos $m=1$, la capacidad $Q$ y la cota $B$ son solo operaciones de adjuntar unos pocos datos escalares. Por lo tanto, el algoritmo que construye $I'$ desde $I$ ejecuta en tiempo $O(n^2)$ (o mejor, dependiendo del formato de entrada), que es polinomial. Esto establece que tenemos una reducción de TSP a VRP en tiempo polinomial. 

La corrección ya fue demostrada: la transformación preserva la respuesta (sí/no) de la instancia. En términos de teoría de la complejidad computacional, hemos demostrado $TSP \le_p VRP$ (reducción polinomial).
Dado que el TSP (versión de decisión) es un problema NP-completo clásico​, esta reducción implica inmediatamente que el VRP (versión de decisión descrita) es NP-difícil (NP-hard). Más específicamente, como TSP $\le_p$ VRP y TSP está en NP-hard, concluimos VRP está en NP-hard​.

Además, VRP claramente pertenece a NP (un certificado puede ser justamente el conjunto de rutas: en tiempo polinomial se puede verificar que cada cliente aparece exactamente una vez, que las rutas no exceden la capacidad y calcular el costo total para comprobar que $\le B$). Por lo tanto, VRP es NP-difícil y está en NP, lo que significa que VRP (decisión) es NP-completo, a menos que se especifique lo contrario alguna variante particular. 

