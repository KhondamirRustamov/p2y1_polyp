import os

init = 'step5_input'
rest_prefix = 'step5_input'
mini_prefix = 'step6.0_minimization'
equi_prefix = 'step6.{}_equilibration'
prod_prefix = 'step7_production'
prod_step   = 'final'


# Minimization

os.system(f'gmx grompp -f step6.0_minimization.mdp -o {mini_prefix}.tpr -c step5_input.gro -r step5_input.gro -p topol.top -n index.ndx -maxwarn 3')
os.system(f'gmx mdrun -v -deffnm {mini_prefix} -nt 12 -pin on -pinoffset 0')


# Equilibration
for i in range(6):
    c = i+1
    istep = f'step6.{c}_equilibration'
    pstep = f'step6.{c-1}_equilibration'
    if c==1:
        pstep = mini_prefix
    os.system(f'gmx grompp -f {istep}.mdp -o {istep}.tpr -c {pstep}.gro -r {rest_prefix}.gro -p topol.top -n index.ndx -maxwarn 5')
    os.system(f'gmx mdrun -v -deffnm {istep} -nt 12 -pin on -pinoffset 0')


os.system(f'gmx grompp -f step7_production.mdp -o final.tpr -c {istep}.gro -p topol.top -n index.ndx -maxwarn 5')
os.system(f'gmx mdrun -v -deffnm final -nt 12 -pin on -pinoffset 0')


