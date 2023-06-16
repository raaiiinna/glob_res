cell_fields = [
    "Density",
    "x-velocity",
    "y-velocity",
    "z-velocity",
    "Pressure",
    "metallicity",
    "H2-fraction",
    "HII-fraction",
    "HeII-fraction",
    "HeIII-fraction"]
epf = [("p1", "double"), ("p2", "double"),("p3", "double"),("p4", "double")]


import yt


#m3.00jw
for x in range(10,18):
    ds = yt.load("/home/rhatcher/scratch/Analysis/Data/m3.00jw/output_000" + str(x) + "/info_000" + str(x) + ".txt",fields=cell_fields, extra_particle_fields=epf)
    ds.field_list
    ds.derived_field_list
    s=yt.ProjectionPlot(ds,"z",("gas","temperature"),weight_field=("gas","density"),buff_size=(800,800))
    s.annotate_particles(width=(5,'pc'))
    s.save('m3.00jw_projection_edge_output_0000' + str(x-8) + '.png')

for x in range(18,26):
    ds = yt.load("/home/rhatcher/scratch/Analysis/Data/m3.00jw/output_000" + str(x) + "/info_000" + str(x) + ".txt",fields=cell_fields, extra_particle_fields=epf)
    ds.field_list
    ds.derived_field_list
    s=yt.ProjectionPlot(ds,"z",("gas","temperature"),weight_field=("gas","density"),buff_size=(800,800))
    s.annotate_particles(width=(5,'pc'))
    s.save('m3.00jw_projection_edge_output_000' + str(x-8) + '.png')
