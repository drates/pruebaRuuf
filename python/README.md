📝 Mi Solución

Una función que compara cuántos paneles caben en distintas orientaciones, llenando los espacios vaciós si es posible, y validando datos (casos que resultado es cero unidades).

¿Cómo desarrollé la solución?

Primero analicé el problema. Sin ser experto en algoritmos, usando mis habilidades analíticas y de geometria, mi razonmiento fue que era necesario simplemente probar
cuántos paneles cabían considerando distitnas orientaciones y llenando si los espacios sobrantes si era posible.

Tengo poca experiencia con Python (Learn Pythn the hardway, hace varios años) y más experiencia reciente con C#. Y ya que el test era con Python o Typescript (que he ocupado para frontend),
resolví pedir a Gemini que me escribiera un códido en Python para la función. Revisé el código, confirmando de que era consistente y bien aplicada la lógica, la que me parece es robusta y eficiente, 
y por lo tanto una solucón adecuada para producción. Además agrega solución rápida para validar casos en que resultado es cero (sin hacer toda la comparación, importante para eficiencia de recursos).

Supuestos interesantes

Un supuesto interesante es que lados de paneles y techo tienen que ser paralelos. Esto simplifica cálculos, pero también es realista (mayoría de techumbres son rectangulares).

Otro supuesto más relevante a nivel práctico es que estammos asumiendo que no se deja un margen de seguridad (para instalación) y estamos ocupando el máximo del techo posible. Sin embargo, 
si el margen mínimo para instalacíón es un valor fijo y no variable, eso se puede simplemente restar el input de dimensiones del techo, lo que no complicaría el cálculo y permitiría usar la misma 
función.

Bonus

Es bueno tener validación de datos (casos que da cero paneles) interna pero el frontend también debería tener lógica para no permitir valores iguales o menores a dimensiones de paneles, 
asegurando que no se hacen cálculos con valores inválidos. Más aún, debería haber una regla de negocio de cantidad de paneles mínimo (dimensiones mínimas del techo) que justifican
prestación de servicio (valor que probablemente es mayor a 1).

Video: no alancé a hacer video pero sería contar lo escrito anteriormente y mostrar consola diciendo wuuf wuuf para casos de test.

