import capytaine as cpt
from capytaine_julia_backend import CapytaineJuliaBackend

mesh = cpt.mesh_sphere().immersed_part()
body = cpt.FloatingBody(mesh, dofs=cpt.rigid_body_dofs())
pb = cpt.RadiationProblem(body=body, wavenumber=1.0, radiating_dof="Heave")

cptjl = CapytaineJuliaBackend()

ref_solver = cpt.BEMSolver(method="direct")
ref_res = ref_solver.solve(pb)

julia_solver = cpt.BEMSolver(engine=cptjl, method="direct")
julia_res = julia_solver.solve(pb)

print(ref_res.forces["Heave"])
print(julia_res.forces["Heave"])

