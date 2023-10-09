class Experiment:
    def __init__(self, sx, sy, gx, gy, b, d, m, sizeX=None, sizeY=None):
        self.startx = sx
        self.starty = sy
        self.goalx = gx
        self.goaly = gy
        self.scaleX = sizeX if sizeX is not None else -1
        self.scaleY = sizeY if sizeY is not None else -1
        self.bucket = b
        self.distance = d
        self.map = m

class ScenarioLoader:
    def __init__(self, fname=None):
        self.experiments = []
        self.scenName = ""

        if fname is not None:
            self.load_scenario(fname)

    def load_scenario(self, fname):
        self.scenName = fname
        experiments = []
        
        with open(fname, 'r') as sfile:
            ver_line = sfile.readline()
            if ver_line.startswith("version"):
                ver = float(ver_line.split()[1])
            else:
                ver = 0.0
                sfile.seek(0)
            
            for line in sfile:
                values = line.split()
                bucket = int(values[0])
                map_file = values[1]
                sx, sy, gx, gy = map(int, values[2:6])
                dist = float(values[-1])
                
                if ver == 0.0:
                    exp = Experiment(sx, sy, gx, gy, bucket, dist, map_file)
                elif ver == 1.0:
                    sizeX, sizeY = map(int, values[6:8])
                    exp = Experiment(sx, sy, gx, gy, bucket, dist, map_file, sizeX, sizeY)
                else:
                    raise ValueError("Invalid version number.")
                
                experiments.append(exp)
        
        self.experiments = experiments

    def save_scenario(self, fname):
        with open(fname, 'w') as ofile:
            ver = 1.0
            ofile.write(f"version {ver}\n")
            
            for exp in self.experiments:
                ofile.write(f"{exp.bucket}\t{exp.map}\t{exp.scaleX}\t{exp.scaleY}\t")
                ofile.write(f"{exp.startx}\t{exp.starty}\t{exp.goalx}\t{exp.goaly}\t{exp.distance}\n")

    def get_num_experiments(self):
        return len(self.experiments)

    def get_scenario_name(self):
        return self.scenName

    def get_nth_experiment(self, which):
        return self.experiments[which]

    def add_experiment(self, experiment):
        self.experiments.append(experiment)

scenario_loader = ScenarioLoader()

scenario_loader.load_scenario('arena.map.scen')

num_experiments = scenario_loader.get_num_experiments()
scenario_name = scenario_loader.get_scenario_name()

print(f"Scenario Name: {scenario_name}")
print(f"Number of Experiments: {num_experiments}")

for i in range(num_experiments):
    experiment = scenario_loader.get_nth_experiment(i)
    print(f"Experiment {i + 1}:")
    print(f"Map: {experiment.map}")
    print(f"Start Coordinates: ({experiment.startx}, {experiment.starty})")
    print(f"Goal Coordinates: ({experiment.goalx}, {experiment.goaly})")
    print(f"Bucket: {experiment.bucket}")
    print(f"Distance: {experiment.distance}")
    print(f"X Scale: {experiment.scaleX}")
    print(f"Y Scale: {experiment.scaleY}")
    print()


