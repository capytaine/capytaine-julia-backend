class CapytaineJuliaBackend:
    def __init__(self):
        from juliacall import Main as jl
        self.jl = jl
        self.jl.seval("using MarineHydro, LinearAlgebra")

    def build_matrices(self, mesh1, mesh2, free_surface, water_depth, wavenumber, gf, adjoint_double_layer):
        if mesh1 is not mesh2:
            raise NotImplementedError()

        if free_surface != 0.0 or water_depth != float('inf'):
            raise NotImplementedError()

        green_functions = (self.jl.Rankine(), self.jl.RankineReflected(), self.jl.GFWu())
        mesh = self.jl.Mesh(mesh1)
        S, D = self.jl.MarineHydro.assemble_matrices_broadcasting(green_functions, mesh, wavenumber, direct=not adjoint_double_layer)
        return S.to_numpy(), D.to_numpy()

    def linear_solver(self, A, b):
        decomp = self.jl.lu(A) 
        x = getattr(self.jl, "\\")(decomp, b)
        return x.to_numpy()
