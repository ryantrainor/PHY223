(TeX-add-style-hook
 "Photoelectric_effect"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "fullpage"
    "amsmath"
    "epsfig"
    "graphics"
    "caption"
    "circuitikz")
   (LaTeX-add-labels
    "fig exp setup"
    "fig detector"
    "fig lines"))
 :latex)

