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

### Modelo matematico 2

### Reduccion HFVRP

- HFVRP (heterogeneous fleet vehicle routing) problem

### Propuesta de algoritmo 2

### Analisis de complejidad algoritmo 2

## Criticas y limitantes
