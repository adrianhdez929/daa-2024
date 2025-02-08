# Problema original

## **Optimización de Ayuda Humanitaria en el Huracán Aurora**

En septiembre de 2023, la región costera de un país ficticio llamado **Costa del Sol** fue devastada por el **Huracán Aurora**, una tormenta de categoría 5 que dejó a su paso inundaciones extremas, carreteras destruidas y más de **50,000 personas afectadas**. La tormenta impactó especialmente a comunidades rurales donde la infraestructura era débil, lo que ocasionó retrasos significativos en la llegada de ayuda humanitaria.

En las primeras **48 horas del desastre**, organizaciones humanitarias como la **Agencia de Respuesta Internacional (ARI)** y las autoridades locales enfrentaron **graves problemas logísticos**:

- **Distribución desigual de recursos:** Centros de distribución enviaron alimentos y medicinas a zonas que no eran las más críticas, mientras que otras áreas quedaron sin suministros esenciales.
- **Infraestructura colapsada:** Las carreteras principales estaban inundadas o bloqueadas por escombros, complicando el transporte y ralentizando la entrega.
- **Falta de predicción de la demanda:** A medida que surgían problemas adicionales, como enfermedades derivadas del agua estancada, la demanda cambió rápidamente, generando un desbalance en la asignación de recursos.

La combinación de estos factores **ralentizó la entrega** de recursos críticos como agua potable, alimentos y medicinas, poniendo **vidas en riesgo** y destacando la necesidad urgente de un sistema eficiente de optimización logística.

La **Agencia de Respuesta Internacional (ARI)** y las autoridades locales enfrentan el desafío de optimizar la distribución de ayuda humanitaria tras el **Huracán Aurora**, con el objetivo de **maximizar la entrega eficiente de recursos** y **minimizar tiempos, costos y riesgos operativos** en una situación crítica. Es necesario determinar qué suministros deben enviarse a cada área priorizando la **gravedad del impacto** y la **población afectada**, mientras se consideran las **limitaciones de transporte y almacenamiento** en centros logísticos para evitar escasez en las zonas más críticas o exceso en áreas menos afectadas. La **infraestructura parcialmente colapsada**, con carreteras inundadas o bloqueadas, obliga a encontrar **rutas alternativas** que reduzcan el tiempo y el costo de transporte para garantizar la entrega rápida de recursos esenciales. Además, es vital anticipar **nuevos riesgos** como réplicas sísmicas, inundaciones adicionales o fallos en el transporte y el personal, implementando **planes de contingencia** que minimicen interrupciones en la cadena de suministro.

## Subproblemas seleccionados

- Luego del huracan Aurora, algunas calles y caminos fueron dañados, impidiendo el paso de las ayudas humanitarias a las zonas afectadas. Se tiene un presupuesto *B*, una cantidad de suministros *S* y un grafo ponderado de la zona afectada.
Se tiene un conjunto *D*, tal que cada *D_i* representa una zona de desastre y una lista *P* tal que *P_i* es la prioridad de la zona *i*.
Se desea saber si existe un conjunto de caminos que se pueden arreglar con el presupuesto *B* tal que el suministro *S* llegue a la mayor cantidad de zonas afectadas posibles, priorizando las zonas de mayor demanda.

- La agencia humanitaria tiene varias sucursales distribuidas en el territorio, representadas por el conjunto S. Cada sucursal i posee una flota heterogénea de vehículos F_i, donde cada vehículo j tiene capacidad de carga c_i_j y consumo d_i_j. Se dispone de un grafo ponderado que modela el mapa de la region afectada, donde algunos nodos pueden ser zonas afectadas o sucursales y dada una arista e, w(e) representa la distancia del viaje entre los nodos extremos.
Cada zona afectada D_k, tiene una demanda especifica de suministros que debe ser satisfecha exactamente una vez por un unico vehiculo. Un vehiculo asignado debe partir de su sucursal de origen y visitar un conjunto de zonas {D_k_1, D_k_2, ...} y regresar a su sucursal. La suma de las demandas q_k en las zonas visitadas por un vehiculo no puede exceder la capacidad c_i_j. De ser necesario no todos los vehiculos deben utilizarse, ya que esto podria minimizar costos. Se desea minimizar el costo de combustible de todos los vehiculos, donde el costo esta dado como: d_i_j * distancia recorrida por F_i_j (vehiculo j de la flota i).

## Subproblema 1

### Modelo matematico 1

Plantear modelo matematico

### Reduccion BMC

- Budgeted maximum coverage problem

### Propuesta de algoritmo 1

### Analisis de complejidad algoritmo 1

## Subproblema 2

Este problema consiste en minimizar los costos de transportacion de recursos desde las sucursales de suministros hacia las zonas afectadas, priorizando las zonas con mayor demanda, puesto que en nuestra modelacion esto implica mayor prioridad.
Dichos costos estan contemplados como combustible y tiempo, de ahi que sea un problema tanto de seleccion de vehiculos, como de otimizacion de rutas.
Se agrega un conjunto de restricciones tanto a los vehiculos, como a las condiciones de seleccion de casos validos, dado que es necesario que se asemeje lo mas posible a las necesidades de un problema de la vida real.

### Modelo matematico 2

#### Dominios

- $S$: Conjunto de sucursales de la agencia humanitaria.
- $F$: Conjunto de flotas, donde $F_i$ representa la flota asociada a la sucursal $i$. Cada vehiculo de la flota tiene las siguientes propiedades:  
  - $c$: Que representa la capacidad de carga del vehiculo.
  - $d$: Que representa el consumo de combustible por unidad de distancia.
- $D$: Conjunto de zonas afectadas. Cada zona tiene una demanda $q$.

#### Definicion del grafo

- $V$ = $S \cup D$: donde los nodos son tanto las sucursales como las zonas afectadas.
- $E$: Las aristas entre dos nodos $i$, $j$ representan que existe un camino de $i$ a $j$. De donde siendo $e$ dicha arista, $w(e)$ representa la distancia de dicho camino.

#### Variables del problema de optimizacion

- $x_{ijkl} \in \{0, 1\}$: Toma el valor 1 si el vehiculo *j* de *F_i* viaja del nodo *l* al nodo *m*.
- $y_{ij} \in \{0, 1\}$: Toma el valor 1 si el vehiculo *j* de *F_i* es utilizado.

#### Funcion objetivo

Definimos la funcion objetivo como el problema de minimizar:
$$
\sum_{i \in S}{\sum_{j \in F_i}{\sum_{k in V}{\sum_{l \in V}{d_j \times w(<k, l>) \times x_{ijkl} \times y_{ij}}}}}
$$

### Reduccion HFVRP

- HFVRP (heterogeneous fleet vehicle routing) problem

Dada una instancia del problema HFVRP (heterogeneous fleet vehicle routing problem) se tiene que:

- $D$: deposito de origen.
- $C$: conjunto de clientes, con necesidades $q$.
- $V$: conjunto heterogeneo (con distintas caracteristicas) de vehiculos, con capacidades $c$ y costos $d$ por unidad de distancia.
- $M$: matriz de distancia que representa el grafo.

El objetivo es asignar rutas a vehiculos, tal que cada vehiculo este asignado a al menos un cliente y todos los clientes tengan una ruta asignada, minimizando el costo total de consumo y distancia.
La funcion de conversion de una instancia de HFVRP a una de nuestro problema, es simplemente definirla tal que la cantidad de nodos de salida (depositos) es igual a 1.
Dado que nuestro problema es una version mas general de HFVRP, dado que la cantidad de depositos de origen es mayor que 1, toda instancia valida de HFVRP es una instancia valida de nuestro problema.
Por tanto nuestro problema es al menos tan complejo como HFVRP, que como el mismo es NP-Hard, nuestro problema es tambien NP-Hard.
  
### Propuesta de algoritmo 2

- **Propuesta Greedy**:

La idea general del algoritmo es asociar zonas afectadas a sucursales.
Inicialmente asumiendo como heuristica la asociacion a la sucursal mas cercana a dicha zona.
Luego se asignan vehiculos a distintas zonas, para crear las rutas, de forma tal que la suma de las demandas no exceda las capacidades, tanto del vehiculo en cuestion como de la flota de la sucursal en cuestion.
Como nuestro modelo original se enfoca en minimizar costos, podemos cambiar dicho enfoque para maximizar ahorros, con lo cual se utiliza una cola de prioridad para ordenar dichos ahorros por ruta, independientemente del deposito.
Luego se van extrayendo las tuplas de ruta y deposito de la cola, verificando si dicha asignacion mejora la ya existente, en cuyo caso se sobreescribe el resultado.

- Correctitud:

- Ejemplo de codigo:

``` python
import sys
import heapq as hq
from scipy.sparse.csgraph import floyd_warshall, dijkstra

'''
Input
F: conjunto de flotas: F[i] = (c, d), asumimos que F[i] esta ordenado bajo el criterio de F[i] >= F[j] si y solo si ci/di >= cj/dj, o sea, la capacidad es mayor que el consumo 
D: conjunto de zonas: D[i] = q
M: matriz de distancia, donde los primeros k nodos representan las sucursales, y los restantes las zonas de desastre, con k = len(F)

Output
A: diccionario de asignacion, donde en la posicion i esta la asignacion de la ruta de la sucursal j, y dicha asignacion esta representada como una lista de los nodos que debe visitar su flota
'''
def assign_routes(F, D, M):
  # se calculan las distancias minimas entre los nodos, asi como las rutas y fuentes de los caminos de costo minimo utilizando dijkstra
  distances, predecessors, sources = dijkstra(csgraph=graph, directed=False, indices=range(len(F)), return_predecessors=True, min_only=True)

  # key = zona
  # value = sucursal
  depot_assign = {}

  # dict que contiene las rutas de cada asignacion
  paths = {}

  # dict que contiene el costo de las demandas de las zonas de la ruta
  path_cost = {}

  # lista que contiene la suma para cada sucursal, la suma de los valores de su respectiva flota
  depot_fleet = [(sum([v[0] for v in f]), sum([v[1] for v in f])) for f in F]

  # lista que contiene las asignaciones de vehiculos a las rutas
  path_assign = []

  # a cada zona se le asocia su sucursal mas cercana
  for i in range(len(F), len(M[0])):
    min_dist = sys.float_info.max
    closest_depot = 0

    for j in range(len(F)):
      if distances[i][j] < min_dist:
        min_dist = distances[i][j]
        closest_depot = j
    depot_assign[i] = closest_depot

  # ordenamos las asignaciones por prioridad
  depot_assign.sort(key=lambda x: D[x[0]], reverse=True)

  # formamos la ruta desde la zona i hasta la sucursal j
  merged = []
  for i, j in depot_assign:
    if i in merged:
      continue
    
    # si existe un camino hacia la sucursal j, se agrega i a dicho camino
    if paths.get(j):
      paths[j].append(i)
      continue

    # se asume que siempre hay camino de i a j
    path = [j]
    current = j

    while current != i:
      current = predecessors[i, current]
      
      if depot_assign[current] == j:
        merged.append(current)

      path.append(current)
      path.reverse()
      paths[j] = path

  # por cada ruta se le calcula el costo total y se verifica si su sucursal puede encargarse de proveer dicha demanda
  for depot, path in paths:
    path_cost[depot] = sum([D[i] if i >= len(F) else 0 for i in path])
    
    # si el costo de la ruta es mayor que la capacidad de la flota de la sucursal entonces se cambia con la sucursal mas cercana que tenga una flota capaz de encargarse de la demanda
    if path_cost[depot] > depot_fleet[depot][0]:
      closest_depots = [i for i in range(len(F))]
      closest_depots.sort(key=lambda x: distances[depot, x])

      valid_depot = False

      for closest in closest_depots:
        if depot_fleet[closest][0] >= path_cost[depot]:
          temp = paths[depot]
          paths[depot] = paths[closest]
          paths[closest] = temp
          break

      if not valid_depot:
        return {}, False
  return paths, True

```

- Analisis de complejidad:

### Analisis de complejidad algoritmo 2

## Criticas y limitantes
