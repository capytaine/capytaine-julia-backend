import capytaine as cpt


class CapytaineJuliaBackend:
    def __init__(self):
        pass

    def build_matrices(self, mesh1, mesh2, free_surface, water_depth, wavenumber, adjoint_double_layer):
        from juliacall import Main as jl
        jl.seval("using MarineHydro")



if __name__ == "__main__":
    body = cpt.FloatingBody(cpt.mesh_sphere(), dofs=cpt.rigid_body_dofs())
    pb = cpt.RadiationProblem(body=body, wavenumber=1.0)

    solver = cpt.BEMSolver(engine=CapytaineJuliaBackend())
    res = solver.solve(pb)
    print(res.forces)

