import matplotlib.pyplot as pl
from figure_panels import *

## Setup figure ##
fig_id = 'fig2'
figw,figh = 3.35,3.5
fig = pl.figure(fig_id, figsize=(figw,figh))

row_bottoms = [.63, .58, .14, .04]
letter_ys = [.97, 0., .45, .44]
letter_xs = [.01, .32, 0, 0.01, .58, .01, .295, .62, 0]
letters = ['a','','','b','c', '','','','']
#letters = [l.upper() for l in letters]

let_kw = dict(fontsize=9, fontname='Arial', weight='bold')

# boxes: row_id, x, w, h (w/h in inches)
boxes       =       [   

                        [ 0, # 1
                          0.1,
                          .7 ,
                          1. ],

                        [ 0, # 2
                          0.42,
                          .7 ,
                          1. ],

                        [ 0, # 3
                          0.74,
                          .7 ,
                          1. ],

                        [  2, # 5
                          0.19,
                          .7 ,
                          1. ],
                        
                        [  2, # 6
                          0.7,
                          .7,
                          1. ],

                        [  3, # 7
                          0.19,
                          .7,
                          .3 ],
                        
                         
                        ]

# draw letters
for lx,letter,(row_id,*_) in zip(letter_xs, letters, boxes):
    fig.text(lx, letter_ys[row_id], letter, **let_kw)
# convert panel w/h to fractions
boxes = [[b[0], b[1], b[2]/figw, b[3]/figh] for b in boxes]
# convert row_ids to y positions
boxes = [[b[1], row_bottoms[b[0]], b[2], b[3]] for b in boxes]
# draw axes
axs = [fig.add_axes(box) for box in boxes]

## Draw panels
axs = regs(axs, panel_id=0, manips=[0,5], ylab=True, hard=False, xlab=False, xrot=90)
axs = regs(axs, panel_id=1, manips=[0,6], ylab=False, hard=False, xlab=True, main_title=True, xrot=90)
axs = regs(axs, panel_id=2, manips=[0,7], ylab=False, hard=False, xlab=False, xrot=90)
axs = reg_difs(axs, panel_id=3, manips=[5,6,7])
axs = light_triggered_regression(axs, panel_id=4)
axs = light_delivery_schematic(axs, panel_id=5, manips=[5,6,7], exclude_phases=[2,3], labelmode=3)

prettify_axes(axs)

pl.savefig('/Users/ben/Desktop/{}.pdf'.format(fig_id), dpi=500)
pl.close('all')