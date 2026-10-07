(TeX-add-style-hook
 "Speed_of_light"
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
    "circuitikz"))
 :latex)

