# Reducción formal del VRP clásico al HFVRP

## Definición del problema VRP clásico

El **Vehicle Routing Problem (VRP)** clásico se define típicamente de la siguiente manera:

- **Grafo de localidades:** Tenemos un conjunto de nodos \(V = \{0,1,2,\dots,n\}\) donde \(0\) representa el **depósito** (centro de distribución) y \(\{1,\dots,n\}\) son los **clientes** (puntos de entrega). Existe un conjunto de aristas que conectan los nodos, con costos de viaje conocidos \(c(i,j)\) para cada par de nodos (por ejemplo, distancias o tiempos entre localidades).
  
- **Demanda de clientes:** Cada cliente \(i \in \{1,\dots,n\}\) tiene una demanda \(d_i > 0\) de cierta mercancía (en el VRP clásico asumimos que la demanda total de cada ruta no excede la capacidad del vehículo).

- **Flota de vehículos homogénea:** Se dispone de \(K\) vehículos **idénticos**, todos con la misma capacidad \(Q\). Todos los vehículos comienzan en el depósito \(0\) y deben regresar al depósito al finalizar su ruta.

- **Restricciones de capacidad:** La suma de las demandas de los clientes atendidos por un mismo vehículo no puede exceder \(Q\). Usualmente, además, cada cliente debe ser atendido *exactamente una vez* por **un** vehículo (no se permiten entregas fraccionadas entre vehículos en la formulación clásica).

- **Objetivo:** Encontrar un conjunto de rutas (una ruta para cada vehículo usado) tal que:  
  1. Cada cliente sea visitado por exactamente un vehículo.  
  2. Ningún vehículo exceda su capacidad \(Q\).  
  3. Todos los vehículos inician y terminan en el depósito.  
  4. Se minimice el costo total de transporte (por ejemplo, la suma de costos/distancias recorridas por todos los vehículos).  

El VRP es un problema notoriamente difícil: se sabe que **es NP-hard** (NP-difícil) porque generaliza al problema del viajante (TSP) como un caso particular. Esto implica que no se conoce ningún algoritmo de tiempo polinomial para resolver el VRP en general (a menos que \(P = NP\)).

---

## Definición del problema HFVRP (flota heterogénea)

El **Heterogeneous Fleet VRP (HFVRP)** extiende el VRP permitiendo una flota con múltiples **tipos de vehículos** con características diferentes. Formalmente, una instancia de HFVRP incluye:

- **Nodos y demandas:** El mismo conjunto de nodos \(V = \{0,1,\dots,n\}\) con un depósito \(0\) y clientes \(1,\dots,n\) con demandas \(d_i\), y la misma matriz de costos de viaje \(c(i,j)\) entre nodos. (El HFVRP generalmente se considera sobre el mismo tipo de grafo que el VRP).

- **Flota heterogénea:** Un conjunto de tipos de vehículos \(T = \{1,2,\dots,m\}\). Cada tipo \(j\in T\) tiene una capacidad \(Q_j\) (máxima carga que puede llevar) y un costo asociado. El costo puede descomponerse, por ejemplo, en un costo por distancia recorrida (o tiempo) y/o un costo fijo por usar un vehículo de ese tipo. Adicionalmente, puede haber una cantidad limitada \(M_j\) de vehículos disponibles de cada tipo \(j\) (flota fija heterogénea). Todos los vehículos comienzan y terminan en el depósito (suponiendo un solo depósito; si hubiera varios, sería una extensión de múltiples depósitos).

- **Restricciones:**  
  1. Cada ruta asignada a un vehículo de tipo \(j\) no puede sobrepasar la capacidad \(Q_j\).  
  2. Cada cliente debe ser atendido exactamente una vez.  
  3. No se puede usar más vehículos de cada tipo que la disponibilidad \(M_j\).  

- **Objetivo:** Diseñar rutas para un subconjunto de vehículos (posiblemente de distintos tipos) de modo que se satisfagan todas las demandas (cada cliente atendido) respetando las capacidades y disponibilidades, y minimizando el costo total de operación (suma de costos de transporte de todas las rutas, incluyendo costos por distancia y cualquier costo fijo por uso de vehículos).

Es claro que el HFVRP es una **generalización** del VRP: si todos los vehículos tienen el mismo tipo (misma capacidad y costos), el HFVRP se reduce al VRP clásico. El HFVRP incluye al VRP como caso especial, por lo que también **es NP-hard** (NP-difícil). En términos de complejidad, agregar heterogeneidad no simplifica el problema; al contrario, mantiene (o aumenta) la dificultad combinatoria al tener que elegir entre diferentes tipos de vehículos en las rutas.

---

## Reducción de una instancia VRP a una instancia HFVRP

Dada una instancia del VRP clásico, podemos **transformarla** en una instancia equivalente de HFVRP de forma directa:

1. **Conjunto de nodos y demandas:** Mantenemos exactamente los mismos clientes, el mismo depósito y las mismas demandas \(d_i\) para cada cliente \(i\). También conservamos la misma matriz de costos \(c(i,j)\) entre nodos que tenía la instancia VRP.

2. **Definición de tipos de vehículo:** Introducimos un conjunto de tipos de vehículos \(T = \{1\}\) con un único tipo de vehículo. A este tipo único le asignamos capacidad \(Q_1 = Q\), donde \(Q\) es la capacidad común de los vehículos en el VRP original. Definimos los costos de este tipo de manera consistente con el VRP original (por ejemplo, costo por unidad de distancia igual al costo unitario en VRP, y si en VRP no había un costo fijo por vehículo, consideramos costo fijo 0 para este tipo).

3. **Disponibilidad de vehículos:** Establecemos \(M_1 = K\), donde \(K\) es el número de vehículos idénticos en la instancia VRP original. Es decir, disponemos de \(K\) vehículos del tipo 1 en la instancia HFVRP.

4. **Restricciones y objetivo:** Las restricciones de capacidad y asignación se mantienen igual (cada ruta con un vehículo tipo 1 puede cubrir hasta \(Q\) de demanda, y cada cliente solo puede aparecer en una ruta). El objetivo sigue siendo minimizar el costo total de las rutas.

Esta construcción produce una instancia de HFVRP que **esencialmente reproduce el mismo espacio de soluciones** que la instancia VRP original. Dado que solo hay un tipo de vehículo en la instancia HFVRP resultante, todas las soluciones posibles involucran únicamente vehículos de ese tipo, los cuales se comportan igual que los vehículos homogéneos del VRP. Cualquier solución factible del VRP original es también una solución factible de la nueva instancia HFVRP, y viceversa. Además, los **costos** de cualquier ruta o conjunto de rutas serán idénticos en ambas instancias. Por tanto, la transformación es en tiempo polinomial y asegura la equivalencia de soluciones.

**Conclusión:** Hemos reducido formalmente VRP a HFVRP mostrando que dada cualquier instancia de VRP podemos construir en tiempo polinomial una instancia de HFVRP cuyo conjunto de soluciones corresponde uno a uno con las soluciones de la instancia VRP. Esto prueba que HFVRP es al menos tan difícil como VRP. Dado que VRP es NP-hard, HFVRP también lo es. La diferencia clave es que HFVRP permite vehículos con **diferentes capacidades y costos**, mientras que el VRP clásico usa vehículos homogéneos.


# Equivalencia entre HFVRP y nuestro problema de transporte de recursos humanitario

Supongamos ahora el **problema de transporte de recursos en escenarios humanitarios** dado por el usuario. En esencia, este problema describe una situación de distribución de ayuda que podemos modelar de manera muy similar al HFVRP. A continuación, establecemos la correspondencia directa entre los elementos del HFVRP y los de dicho escenario humanitario:

- **Depósitos (centros de suministro):** En el escenario humanitario, existen uno o varios depósitos o almacenes donde se acopian los recursos de ayuda. Denotemos por \(D\) el conjunto de depósitos disponibles. En la correspondencia con HFVRP, cada depósito en \(D\) corresponde al **depósito** (o depósitos) del modelo de enrutamiento. (Si en el HFVRP original solo se considera un depósito central, podemos asimilar todos los suministros a un único depósito central en el escenario. Si hay varios depósitos, equivale a la extensión multi-depósito de HFVRP).

- **Zonas afectadas con demanda:** El escenario humanitario incluye un conjunto de **zonas afectadas** con demandas de ayuda. Podemos denotar este conjunto de destinos como \(Z = \{1,2,\dots,n\}\), donde cada zona \(i\) tiene una **demanda** \(d_i\). Esta corresponde exactamente al conjunto de **clientes** con demanda en el HFVRP.

- **Flota heterogénea de vehículos:** En la logística humanitaria suele haber varios **vehículos de transporte** (camiones, camionetas, helicópteros, etc.) con diferentes capacidades de carga y costos operativos. Esto se corresponde directamente con la flota heterogénea del HFVRP. Podemos definir un conjunto de tipos de vehículo \(T = \{1,2,\dots,m\}\) donde cada tipo \(j\) representa un vehículo con capacidad \(Q_j\) y un costo de operación particular. Además, puede haber un límite \(M_j\) en la cantidad de vehículos disponibles de cada tipo.

- **Costos de transporte:** En el escenario humanitario, se asocia un costo de transporte a cada recorrido entre dos puntos, normalmente proporcional a la distancia o tiempo. Esto define una matriz de costos \(c(u,v)\) entre cualquier par de ubicaciones \(u\), \(v\). Esta matriz de costos es **idéntica** a la usada en HFVRP.

- **Rutas de entrega válidas (restricciones):**  
  1. Cada vehículo no puede transportar más de su capacidad.  
  2. Cada zona afectada debe ser atendida una sola vez.  
  3. No se puede usar más vehículos de un tipo que los disponibles.  
  4. Todas las rutas inician en un depósito y (típicamente) regresan a un depósito.

  Estas son precisamente las restricciones del HFVRP.

- **Objetivo de optimización:** El objetivo en el escenario humanitario es **minimizar el costo total de la operación de transporte**, lo cual coincide con la minimización del costo total de las rutas en HFVRP.

Dados los puntos anteriores, podemos ver que **existe una correspondencia uno a uno** entre cualquier instancia de HFVRP y el problema humanitario: “clientes” \(\leftrightarrow\) zonas afectadas, “depósito” \(\leftrightarrow\) centro de suministro, y “vehículos heterogéneos” \(\leftrightarrow\) medios de transporte disponibles.

Así, podemos **reducir** HFVRP al problema humanitario y viceversa, simplemente reinterpretando los nodos, las flotas y los costos. Cualquier solución factible en el contexto humanitario es también una solución factible de HFVRP, y toda solución factible de HFVRP corresponde a una solución en el contexto humanitario. Esta transformación es polinomial en el tamaño de la instancia.

Por lo tanto, el problema de transporte de recursos en escenarios humanitarios es **al menos tan difícil** como HFVRP. Dado que HFVRP es NP-hard, el problema humanitario también lo es. En consecuencia, no existe un método en tiempo polinomial que resuelva el problema de manera exacta en todos los casos (a menos que \(P = NP\)), lo que justifica la búsqueda de métodos heurísticos o aproximados en instancias grandes.


