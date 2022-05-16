> Programme fait par : Félix TERRIEN / Raphaël ZRIBI / Gabriel PONS

**Quel était votre projet initial ?**

Notre but était de développer un prototype de notre projet `Sévigné Drawing Bot` afin de s'imager son fonctionnement avant de procéder à la conception sur Arduino. Le projet `Sévigné Drawing Bot` est un robot automatisé qui pourrait reproduire une image ou un tracé numérique sur n’importe quel tableau. Le système serait portable et facile d’utilisation.


**Le programme fonctionne-t-il ? L’avez-vous éventuellement enrichi ?**

Oui, le programme est fonctionnel et nous avons réussi à coder ce qui pourrait s'apparenter au fonctionnement de notre robot. Nous avons donc conçu un programme capable de retranscrire n'importe quelle image en une version dessinable en noir et blanc. Pour cela nous avons utilisé [OpenCV](https://opencv.org) pour appliquer un filtre à l'image afin de la rendre dessinable puis **turtle** afin de dessiner l'image d'une façon semblable à celui de notre robot.


**Quelles difficultés avez-vous rencontré ?**

Nous avons rencontré deux difficultés. La principale fut de retranscrire l'image de manière rapide. En effet, il ne faut pas que turtle dessine pixel par pixel mais par forme, cette problématique n'a pas encore été résolue et nous y travaillons. Enfin, la dernière difficulté que nous avons rencontrée a été de trouver comment scanner la photo.  Du fait que les coordonnées étaient différentes entre *turtle* et *cv2*, le `0.0` de turtle se situe au milieu tandis que celui d'OpenCV se situe en haut à gauche. Par conséquent les premiers essais ne fonctionnaient pas du tout et nous avons donc dû adapter le programme afin que les deux se coïncident.
