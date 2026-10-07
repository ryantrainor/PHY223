(TeX-add-style-hook
 "Writing_A_Report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("xcolor" "dvipsnames")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "fullpage"
    "amsmath"
    "epsfig"
    "graphics"
    "caption"
    "hyperref"
    "parskip"
    "mdframed"
    "xcolor"
    "enumitem"
    "amssymb")
   (LaTeX-add-labels
    "sec:pre-chk"
    "sec:order"
    "sec:Abstract"
    "sec:Introduction"
    "sec:Theory"
    "sec:Methods"
    "Fig: Experimental setup"
    "sec:Data"
    "fig spectrum selectivity"
    "sec:Conclusion"
    "sec:References"
    "sec:post-chk"
    "sec:style")
   (LaTeX-add-environments
    "graybox")
   (LaTeX-add-enumitem-newlists
    '("todolist" "itemize")))
 :latex)

