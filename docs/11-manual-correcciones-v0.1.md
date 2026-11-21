# GHRT: manual de correcciones del documento maestro v0.1

Fecha de revisión: 21 de octubre de 2026.

Documento de referencia: [GHRT_Documento_Maestro_v0.1.pdf](/Users/edwardflores/Downloads/GHRT_Documento_Maestro_v0.1.pdf), 36 páginas. Las páginas indicadas corresponden a esa versión; después de exportar pueden cambiar. Localiza también cada corrección por su sección.

Objetivo: preparar una edición corregida, sugerida como **v0.1.1**, con fórmulas consistentes, supuestos explícitos y tablas legibles. El manual contiene instrucciones editoriales y párrafos de reemplazo.

Las seis observaciones de la revisión tienen distinta naturaleza: hay una fórmula de fuerza incompleta, una ambigüedad entre potencial y lagrangiano, una limitación del ejemplo periódico, una dimensión sin declarar, una estimación que necesita precisar su régimen de validez y errores de edición. Corregir el documento no resuelve por sí mismo las cuestiones abiertas de naturalidad, screening y energía oscura.

## 1. Orden de aplicación

| Código | Página original | Sección | Cambio |
| --- | --- | --- | --- |
| C1 | 13 | 9. Quinta fuerza | Añadir el factor radial de la fuerza de Yukawa y sus supuestos. |
| C2 | 20; definición complementaria en 12 y 14 | 16.1; 8 y 10 | Definir la densidad y corregir la expresión del potencial ambiental. |
| C3 | 20 | 16.1 | Explicar qué hace y qué no hace el ejemplo periódico con \(\varepsilon>0\). |
| C4 | 20 y 31 | 16.2 y 27.3 | Declarar la dimensión de \(\varepsilon_H\). |
| C5 | 15 | 11.2 | Precisar la validez de la estimación del symmetron. |
| C6 | 17 y 31–33 | 13.1, 27.1 y 28 | Reparar fórmulas, tabla y numeración. |

Aplica primero las convenciones del apartado siguiente. Después incorpora C1–C6 y realiza la revisión de exportación del apartado 9.

## 2. Convenciones que deben quedar explícitas

Añadir al bloque «Convenciones del documento», en la página 3:

> Salvo cuando se restituyan expresamente las constantes, usamos unidades naturales \(c=\hbar=1\). La firma métrica es \((-+++)\), \(M_{\rm Pl}\) es la masa de Planck reducida y \(\widetilde g_{\mu\nu}=A^2(\chi)g_{\mu\nu}\), con \(A(\chi)>0\). Definimos \(\alpha=d\ln A/d\chi\) y \(\beta=M_{\rm Pl}\alpha\). Las ecuaciones de fondo de la sección 10 están escritas en el marco de Einstein.

Esto permite que \(m_{\rm eff}r\) sea adimensional. Si se trabaja con una masa en unidades SI, el argumento correspondiente es \(m_{\rm eff}cr/\hbar\).

En los fragmentos LaTeX de este manual se presupone la disponibilidad de los paquetes amsmath y amssymb. Los bloques de código son instrucciones para el archivo fuente; no deben aparecer impresos como código en el PDF científico.

## 3. C1: fuerza de Yukawa completa

**Dónde:** página 13, comienzo de la sección 9.

**Acción:** sustituir la fórmula y los párrafos que la presentan por el siguiente texto.

> Definiendo \(\beta(\chi)=M_{\rm Pl}\,d\ln A/d\chi\), consideramos el límite estático y lineal alrededor de un fondo aproximadamente homogéneo. Para dos cuerpos puntuales con acoplamientos efectivos iguales y una masa ambiental aproximadamente constante, la magnitud de la fuerza escalar respecto de la fuerza newtoniana de referencia es
>
> \[
> \frac{F_\chi}{F_N}
> =2\beta_{\rm eff}^{\,2}(1+m_{\rm eff}r)e^{-m_{\rm eff}r}.
> \]
>
> El factor \(1+m_{\rm eff}r\) aparece al derivar el potencial de Yukawa, proporcional a \(e^{-m_{\rm eff}r}/r\). Puede omitirse como aproximación a distancias pequeñas frente al rango del campo, \(m_{\rm eff}r\ll1\). Para cuerpos con cargas escalares distintas, el producto de sus acoplamientos sustituye al cuadrado de un acoplamiento común. En cuerpos extensos o apantallados, las cargas efectivas deben obtenerse de la solución del campo y de las condiciones de contorno.

Fórmula para LaTeX:

~~~latex
\[
\frac{F_\chi}{F_N}
=2\beta_{\rm eff}^{\,2}
\bigl(1+m_{\rm eff}r\bigr)e^{-m_{\rm eff}r}.
\]
~~~

**Comprobación:** para \(m_{\rm eff}r\to0\), el cociente tiende a \(2\beta_{\rm eff}^2\). Para \(m_{\rm eff}r=1\), el factor radial completo es \(2/e\); la expresión anterior daba \(1/e\).

Aquí \(F_N\) es la referencia newtoniana definida en el mismo marco y normalización. La fórmula no sustituye el cálculo de una geometría experimental concreta.

## 4. C2: potencial ambiental y definición de densidad

**Dónde:** página 20, sección 16.1. Añadir también la definición de densidad junto al potencial efectivo de la sección 8.

La frase «el término ambiental \(T\ln A\) modifica el potencial» es ambigua. Con las convenciones de la acción, la ecuación escalar es

\[
\Box\chi=U_{,\chi}-\alpha T_{\rm E}.
\]

Si \(T_{\rm E}\) se tratara como una fuente externa fija, integrar el término de fuerza daría \(-T_{\rm E}\ln A\) en el potencial. Pero la densidad de materia del sistema acoplado depende de \(\chi\); para polvo conviene escribir su dependencia completa.

### Definición que se debe añadir

> Para materia no relativista distinguimos la densidad física de Einstein, \(\rho_{\rm E}\), de la densidad auxiliar \(\rho_*=\rho_{\rm E}/A=A^3\widetilde\rho\), donde \(\widetilde\rho\) es la densidad de Jordan. Al variar el campo a distribución de partículas fijada, \(\rho_*\) se mantiene independiente de \(\chi\). El potencial efectivo que determina la fuerza escalar puede escribirse como
>
> \[
> U_{\rm eff}(\chi;\rho_*)
> =U(\chi)+\rho_*[A(\chi)-1].
> \]
>
> En consecuencia,
>
> \[
> U_{{\rm eff},\chi}
> =U_{,\chi}+\rho_*A_{,\chi}
> =U_{,\chi}+\alpha\rho_{\rm E}.
> \]

Código:

~~~latex
\[
\rho_*=\frac{\rho_{\rm E}}{A}
      =A^3\widetilde{\rho},
\qquad
U_{\rm eff}(\chi;\rho_*)
=U(\chi)+\rho_*\bigl[A(\chi)-1\bigr].
\]
\[
U_{{\rm eff},\chi}
=U_{,\chi}+\rho_*A_{,\chi}
=U_{,\chi}+\alpha\rho_{\rm E}.
\]
~~~

La resta de \(\rho_*\) elimina un término independiente de \(\chi\) **solo al calcular la fuerza escalar**. No elimina la energía de materia de la ecuación de Friedmann, ni implementa sequestering.

### Ajuste en la sección 8

Identificar la \(\rho\) de su potencial efectivo con \(\rho_*\), y escribir:

~~~latex
\[
U_{\rm eff}
=U_0+\frac{1}{2}
\left(\frac{\rho_*}{M^2}-\mu^2\right)\chi^2
+\frac{\lambda}{4}\chi^4,
\qquad
\rho_{*,c}=\mu^2M^2.
\]
~~~

Se puede conservar el símbolo abreviado \(\rho\) si se declara expresamente que en esa sección representa \(\rho_*\). No hay que sustituir indiscriminadamente todas las densidades del documento.

### Ajuste en la sección 10

Declarar que las densidades que aparecen directamente en Friedmann son las de Einstein. Para polvo:

~~~latex
\[
\dot{\rho}_{\rm E}+3H\rho_{\rm E}
=\alpha\dot{\chi}\rho_{\rm E},
\qquad
\dot{\rho}_*+3H\rho_*=0.
\]
~~~

Estas identidades explican la diferencia entre ambas variables. Mantener el signo de la ecuación escalar de fondo de la página 14: ya es consistente con la acción.

El tratamiento de marcos y densidades puede contrastarse con las secciones 2 y 3.1 de [Symmetron Cosmology](https://arxiv.org/html/1107.2112v1).

## 5. C3: alcance del ejemplo periódico

**Dónde:** página 20, sección 16.1.

**Acción recomendada para una revisión editorial:** conservar las funciones candidatas y reemplazar la explicación de su comportamiento por el texto siguiente. El objetivo es expresar exactamente lo que esas funciones permiten afirmar.

> Consideramos, como ejemplo exploratorio,
>
> \[
> U(\chi)=\Lambda_\chi^4[1-\cos(\chi/f)],
> \qquad
> A(\chi)=\exp\{\varepsilon[1-\cos(\chi/f)]\}.
> \]
>
> Para polvo, el potencial efectivo es \(U+\rho_*[A-1]\). Con \(\varepsilon>0\), \(\rho_*\ge0\) y \(\Lambda_\chi^4>0\), ambos términos tienen sus mínimos en \(\chi=2\pi n f\), con \(n\) entero. La densidad aumenta la curvatura alrededor de esos mínimos:
>
> \[
> m_{\rm eff}^2
> =\frac{\Lambda_\chi^4+\varepsilon\rho_*}{f^2}.
> \]
>
> Por tanto, este ejemplo no produce una transición de restauración y ruptura de simetría al diluirse la materia. Además, \(\alpha=(\varepsilon/f)\sin(\chi/f)\) se anula en esos mínimos para cualquier densidad. Una activación ambiental de tipo symmetron requeriría otra elección de funciones o parámetros y un análisis explícito de mínimos, estabilidad y cargas escalares. La periodicidad conserva una simetría discreta; por sí sola no garantiza protección radiativa suficiente.

Código de las dos expresiones nuevas:

~~~latex
\[
m_{\rm eff}^2\big|_{\chi=2\pi n f}
=\frac{\Lambda_\chi^4+\varepsilon\rho_*}{f^2},
\qquad n\in\mathbb{Z}.
\]
\[
\alpha(\chi)
=\frac{\varepsilon}{f}\sin(\chi/f).
\]
~~~

La ausencia de esa transición no demuestra que toda dinámica cosmológica del campo sea imposible: puede haber evolución fuera del mínimo. Tampoco excluye otras funciones periódicas. La conclusión anterior corresponde específicamente al ejemplo escrito y al signo \(\varepsilon>0\).

**Si se quiere cambiar el modelo:** especificar primero el nuevo \(U\), el nuevo \(A\), los signos y el intervalo de parámetros. Después resolver \(U_{{\rm eff},\chi}=0\), clasificar los extremos con \(U_{{\rm eff},\chi\chi}\) y comprobar la fuerza efectiva en cada ambiente. Cambiar automáticamente el signo de \(\varepsilon\) no constituye una solución demostrada.

## 6. C4: dimensión del portal Higgs periódico

**Dónde:** página 20, sección 16.2, y tabla de parámetros de la página 31.

El operador puede conservarse. La corrección mínima consiste en declarar que su coeficiente tiene dimensión de masa al cuadrado.

Texto para añadir inmediatamente después del portal:

> En esta expresión, \(\varepsilon_H\) es un coeficiente de dimensión de masa al cuadrado, mientras que \(\varepsilon\), usado en el factor conforme, es adimensional. En cuatro dimensiones, \(H^\dagger H\) tiene dimensión de masa al cuadrado y el factor periódico es adimensional, por lo que \(V_{H\chi}\) tiene la dimensión de una densidad de energía. La condición de spurion describe su papel en la ruptura de simetría y no obliga a que sea adimensional.

Código:

~~~latex
\[
V_{H\chi}
=\varepsilon_H(H^\dagger H)
\left[1-\cos\left(\frac{\chi}{f}\right)\right],
\qquad
[\varepsilon_H]=\mathrm{masa}^{2},
\qquad
[\varepsilon]=1.
\]
~~~

En la tabla de parámetros, separar la fila conjunta:

| Símbolo | Definición | Dimensión en unidades naturales |
| --- | --- | --- |
| \(\varepsilon\) | Coeficiente del exponente de \(A(\chi)\) | Adimensional |
| \(\varepsilon_H\) | Coeficiente del portal periódico mostrado | Masa² |

**Alternativa, solo si se desea un coeficiente adimensional:** definir un símbolo nuevo \(\widehat\varepsilon_H\) y una escala \(\mathcal M_H\), con \(\varepsilon_H=\widehat\varepsilon_H\mathcal M_H^2\). Declarar la escala; no omitirla ni identificarla con otra sin justificarlo.

Comprobación de normalización alrededor de \(\chi=0\), después de la ruptura electrodébil:

~~~latex
\[
H^\dagger H=\frac{v^2}{2},
\qquad
1-\cos(\chi/f)
=\frac{\chi^2}{2f^2}
+\mathcal{O}(\chi^4/f^4),
\]
\[
\delta m_\chi^2
=\frac{\varepsilon_H v^2}{2f^2}.
\]
~~~

Esta última expresión corresponde al portal periódico. No reemplaza la estimación \(\delta m_\chi^2=\lambda_{H\chi}v^2\) del portal polinómico de la sección 14.1.

## 7. C5: alcance de la estimación del symmetron

**Dónde:** página 15, sección 11.2.

**Acción:** conservar el párrafo inicial sobre el resultado de la literatura. Sustituir la estimación posterior por este bloque, que explicita el límite de la expansión utilizada.

> Para el potencial polinómico en vacío, con \(\mu^2>0\) y \(\lambda>0\), definimos
>
> \[
> \chi_0=\frac{\mu}{\sqrt{\lambda}},
> \qquad
> \Delta U=U(0)-U(\chi_0)=\frac{\mu^4}{4\lambda},
> \qquad
> \rho_{*,c}=\mu^2M^2.
> \]
>
> Estas expresiones implican
>
> \[
> \frac{\Delta U}{\rho_{*,c}}
> =\frac{\chi_0^2}{4M^2}.
> \]
>
> Si la transición ocurre cerca de la época actual y se intenta identificar la profundidad del potencial con una densidad de energía oscura comparable a la densidad crítica de transición, se necesita \(\chi_0/M\) de orden unidad. En ese régimen, la expansión \(A=1+\chi^2/(2M^2)+\mathcal O(\chi^4/M^4)\) deja de estar controlada. Si se exige \(\chi_0/M\ll1\), la profundidad \(\Delta U\) es mucho menor que \(\rho_{*,c}\).
>
> La elección ilustrativa \(M\sim M_{\rm Pl}\), \(\mu\sim H_0\) y \(\lambda\sim H_0^2/M_{\rm Pl}^2\), del orden de \(10^{-120}\), también lleva a \(\chi_0\sim M\). Es una estimación dimensional, no una región viable demostrada del modelo truncado. La rama estándar compatible con pruebas locales utiliza escalas de acoplamiento menores que \(M_{\rm Pl}\), bajo los supuestos de esos análisis. [R4]
>
> Además, \(\Delta U\) es una diferencia de potencial y no determina por sí sola una densidad positiva de energía oscura: \(U(\chi_0)=U_0-\Delta U\). Elegir \(U_0\) para obtener el valor observado deja pendiente la explicación de esa constante y de su estabilidad radiativa.

Código de la identidad central:

~~~latex
\[
\chi_0=\frac{\mu}{\sqrt{\lambda}},
\qquad
\Delta U=\frac{\mu^4}{4\lambda},
\qquad
\rho_{*,c}=\mu^2M^2,
\]
\[
\frac{\Delta U}{\rho_{*,c}}
=\frac{\chi_0^2}{4M^2}.
\]
~~~

La identidad se obtiene directamente de las funciones del documento. La conclusión sobre la rama estándar y sus restricciones se contrasta con [Symmetron Cosmology, sección 2](https://arxiv.org/html/1107.2112v1).

Si se decide postular que \(A=1+\chi^2/(2M^2)\) es una función exacta para cualquier campo, hay que declarar esa hipótesis y estudiar de nuevo su validez como EFT y sus correcciones. No se deduce de haber escrito una expansión aproximada.

## 8. C6: reparación de ecuaciones y tablas

### 8.1 Filtro de degravitation: página 17

Reemplazar la condición dañada que sigue a \(G_{\rm eff}(k\to0)\). Para el esquema estático en términos de escala espacial:

~~~latex
\[
G_{\rm eff}(k)\longrightarrow 0
\quad\text{cuando }kL\longrightarrow0,
\qquad
G_{\rm eff}(k)\longrightarrow G_N
\quad\text{cuando }kL\gg1.
\]
~~~

Añadir:

> Aquí \(k\) es un número de onda espacial y \(L\) la longitud característica del filtro. La expresión representa el comportamiento deseado por escalas; no define por sí sola un operador covariante, una prescripción causal ni una acción completa.

Si se conserva la notación \(G_{\rm eff}(\Box)\), insertar \(\Box\) como símbolo matemático, no como un carácter ausente de la fuente tipográfica.

### 8.2 Matriz de 50 problemas: páginas 32–33

Reconstruir las celdas matemáticas como ecuaciones. Las secuencias literales de delimitadores y comandos matemáticos que aparecen en el PDF son código sin procesar.

Reparaciones concretas:

| Fila | Acción |
| --- | --- |
| 15, «Materia relativista» | Reunir la expresión completa en la columna «Formalismo»: \(\lvert T\rvert/\rho=\gamma^{-2}\), para la población isotrópica monoenergética indicada en la sección 7.2. Retirar los fragmentos que se desplazaron a otras columnas. |
| 21, «Principio de equivalencia» | Sustituir \(A(\chi)g_{\mu\nu}\) por \(\widetilde g_{\mu\nu}=A^2(\chi)g_{\mu\nu}\), para mantener la definición del documento. |
| 34, «Tiempo» | Unificar con la convención de fase de la sección 19: \(d\varphi=-mc^2d\tau/\hbar\). La frecuencia positiva de referencia sigue siendo \(\omega_C=mc^2/\hbar\). |
| Todas | Confirmar que cada fila conserva seis columnas y que ninguna fórmula ha ocupado la columna «Mapa inicial». |

Código para la fila 15:

~~~latex
\(\lvert T\rvert/\rho=\gamma^{-2}\)
~~~

Si la tabla fuente está en Markdown, utilizar los comandos `\lvert` y `\rvert` evita introducir barras verticales literales que puedan confundirse con separadores de columnas. No reconstruir un porcentaje perdido a partir de una fórmula desplazada: consultar la fuente original o marcarlo como «pendiente».

Los porcentajes existentes, si se conservan como material histórico, deben mantener el aviso de que son estimaciones informales. La reparación tipográfica no los convierte en probabilidades científicas.

### 8.3 Numeración: página 31

La lista de «27.1 Derivación analítica» empieza en 9 y termina en 16. Como programa independiente, reiniciarla en 1 y terminar en 8. Si se pretendía continuar otra lista, hacer explícita esa relación.

### 8.4 Fórmulas en Word, LibreOffice o LaTeX

- **LaTeX:** insertar los fragmentos en el archivo fuente, con delimitadores matemáticos y los paquetes necesarios. No pegar las marcas de bloque Markdown.
- **Word o LibreOffice:** insertar las ecuaciones mediante el editor de ecuaciones y su sintaxis admitida. Pegar comandos LaTeX en texto ordinario no garantiza su conversión.
- **Tablas largas:** repetir encabezados, evitar cortes que separen partes de una fórmula y comprobar la legibilidad al tamaño real de lectura. Si hace falta, repartir la matriz en más páginas.

## 9. Regeneración y comprobación del PDF

1. **Abrir el documento fuente que generó el PDF.** El archivo [manuscript/GHRT.tex](/Users/edwardflores/Projects/Universum/GHRT/manuscript/GHRT.tex) disponible en este proyecto contiene actualmente un documento vacío; todavía no contiene las 36 páginas del maestro. Para regenerarlas se necesita aplicar este manual al fuente completo o transcribir primero su contenido.
2. **Guardar una copia de trabajo con versión nueva**, por ejemplo GHRT_Documento_Maestro_v0.1.1, manteniendo la v0.1 como referencia.
3. **Aplicar C1–C6** por sección y actualizar las convenciones y la tabla de parámetros. Conservar el carácter exploratorio de la rama periódica.
4. **Buscar todas las repeticiones** de la fuerza de Yukawa, del término ambiental con traza, del portal periódico y de la métrica conforme. Revisar cada coincidencia antes de cambiarla.
5. **Componer las ecuaciones y reconstruir las celdas dañadas** con el sistema matemático del editor elegido.
6. **Actualizar portada, fecha, índice y numeración**, y exportar el PDF.
7. **Leer el PDF exportado**, especialmente las páginas que contengan las secciones 8–11, 13.1, 16 y la matriz. La apariencia del archivo fuente no basta.
8. **Corregir cualquier defecto detectado y volver a exportar.**

### Lista de aceptación

- [ ] La fuerza incluye \((1+m_{\rm eff}r)e^{-m_{\rm eff}r}\), o se declara expresamente el límite que permite simplificarla.
- [ ] Las densidades \(\rho_{\rm E}\), \(\rho_*\) y \(\widetilde\rho\) están definidas y no se intercambian sin transformar.
- [ ] El potencial ambiental para polvo tiene derivada \(U_{,\chi}+\alpha\rho_{\rm E}\).
- [ ] La resta constante en \(U_{\rm eff}\) no se presenta como eliminación de energía gravitante.
- [ ] El ejemplo periódico con \(\varepsilon>0\) no se presenta como una transición symmetron ya obtenida.
- [ ] La dimensión de \(\varepsilon_H\) aparece tanto en el texto como en la tabla.
- [ ] La estimación \(\lambda\sim10^{-120}\) conserva la advertencia sobre el régimen de validez.
- [ ] Se distingue \(\Delta U\) de la energía absoluta \(U_0-\Delta U\).
- [ ] La condición del filtro muestra \(kL\gg1\) para recuperar \(G_N\).
- [ ] Las filas 15, 21 y 34 están reparadas y la matriz conserva sus columnas.
- [ ] No quedan comandos matemáticos impresos como texto, caracteres ausentes ni ecuaciones recortadas.
- [ ] El índice, la versión y la fecha corresponden al archivo exportado.

### Texto sugerido para el historial de cambios

> **v0.1.1 — Correcciones matemáticas y editoriales.** Se completa la expresión de la fuerza de Yukawa, se explicitan las densidades y el potencial efectivo, se delimita el alcance del ejemplo periódico, se declara la dimensión del portal Higgs periódico y se precisa el régimen de validez de la estimación del symmetron. Se reparan la notación del filtro, las ecuaciones de la matriz y la numeración. Permanecen abiertos los problemas de naturalidad, implementación del screening y viabilidad cosmológica.

## 10. Referencia técnica

K. Hinterbichler, J. Khoury, A. Levy y A. Matas, *Symmetron Cosmology*, Physical Review D **84**, 103521 (2011), [arXiv:1107.2112](https://arxiv.org/abs/1107.2112), [DOI:10.1103/PhysRevD.84.103521](https://doi.org/10.1103/PhysRevD.84.103521).

Las correcciones sobre el ejemplo periódico, la normalización del portal y el cociente \(\Delta U/\rho_{*,c}\) se obtienen aquí de las funciones y convenciones del documento maestro. No deben atribuirse a esa referencia como propuestas específicas de GHRT.
