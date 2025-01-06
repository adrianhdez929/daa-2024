# Problema

## **Optimización de Ayuda Humanitaria en el Huracán Aurora**

En septiembre de 2023, la región costera de un país ficticio llamado **Costa del Sol** fue devastada por el **Huracán Aurora**, una tormenta de categoría 5 que dejó a su paso inundaciones extremas, carreteras destruidas y más de **50,000 personas afectadas**. La tormenta impactó especialmente a comunidades rurales donde la infraestructura era débil, lo que ocasionó retrasos significativos en la llegada de ayuda humanitaria.

En las primeras **48 horas del desastre**, organizaciones humanitarias como la **Agencia de Respuesta Internacional (ARI)** y las autoridades locales enfrentaron **graves problemas logísticos**:

- **Distribución desigual de recursos:** Centros de distribución enviaron alimentos y medicinas a zonas que no eran las más críticas, mientras que otras áreas quedaron sin suministros esenciales.
- **Infraestructura colapsada:** Las carreteras principales estaban inundadas o bloqueadas por escombros, complicando el transporte y ralentizando la entrega.
- **Falta de predicción de la demanda:** A medida que surgían problemas adicionales, como enfermedades derivadas del agua estancada, la demanda cambió rápidamente, generando un desbalance en la asignación de recursos.

La combinación de estos factores **ralentizó la entrega** de recursos críticos como agua potable, alimentos y medicinas, poniendo **vidas en riesgo** y destacando la necesidad urgente de un sistema eficiente de optimización logística.

La **Agencia de Respuesta Internacional (ARI)** y las autoridades locales enfrentan el desafío de optimizar la distribución de ayuda humanitaria tras el **Huracán Aurora**, con el objetivo de **maximizar la entrega eficiente de recursos** y **minimizar tiempos, costos y riesgos operativos** en una situación crítica. Es necesario determinar qué suministros deben enviarse a cada área priorizando la **gravedad del impacto** y la **población afectada**, mientras se consideran las **limitaciones de transporte y almacenamiento** en centros logísticos para evitar escasez en las zonas más críticas o exceso en áreas menos afectadas. La **infraestructura parcialmente colapsada**, con carreteras inundadas o bloqueadas, obliga a encontrar **rutas alternativas** que reduzcan el tiempo y el costo de transporte para garantizar la entrega rápida de recursos esenciales. Además, es vital anticipar **nuevos riesgos** como réplicas sísmicas, inundaciones adicionales o fallos en el transporte y el personal, implementando **planes de contingencia** que minimicen interrupciones en la cadena de suministro.

## Subproblemas

- Dada una red de flujo, donde *s* (nodo fuente) representa la cantidad de suministros disponibles en los centros de distribución y *t* (nodo objetivo) representa una zona de desastre. Cada arista en la red, representa la capacidad máxima de recursos que se pueden distribuir en un tiempo razonable (digamos un día) por la arista. Dicha capacidad se ve afectada tambien por la calidad de la carretera en cuestión y qué tanto se afectó por el fenómeno. El objetivo es determinar por cada punto de desastre, cuál sería la mayor cantidad de suministros a enviar en un tiempo razonable desde los centros de distribución.
- Dado un grafo dirigido y ponderado que representa un mapa con sus respectivas calles, un conjunto *T* que representa los nodos objetivos, tal que cada *t* tiene asignado un entero *t_k*, y un conjunto *S* que representa los centros de distribución, los cuales tienen una cantidad de suministros y un conjunto de vehículos para transportarlos. Se desea encontrar una solución óptima, tal que maximice la equidad en la distribución de los suministros, disminuyendo el costo de transportación. Se asume que el peso de una arista *(v, u)* representa el gasto de combustible de un vehículo que va del nodo *v* al nodo *u*.

## Importancia práctica

Las redes de distribución de suministros son fundamentales en la logística de emergencias, permitiendo la entrega eficiente de recursos críticos en situaciones de desastre. 
Usualmente este trabajo es realizado por organizaciones humanitarias o autoridades locales, por lo que es necesario encontrar una solución que reduzca tanto el costo como el tiempo de transportación, así como maximizar la equidad en la distribución de los suministros.