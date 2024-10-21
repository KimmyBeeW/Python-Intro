import matplotlib.pyplot as plt


def convert_row_type(nums):
    return [float(num) for num in nums]


def plot_histogram():
    with open("admission_algorithms_dataset.csv", 'r') as infile:
        lines = infile.readlines()
        sat_list = []
        gpas = []
        for line in lines[1:]:
            line = line.strip('\n').split(',')
            sat, gpa = convert_row_type(line[1:3])
            sat_list.append(sat)
            gpas.append(gpa)

    plt.hist(gpas)
    plt.savefig("gpa.png")
    plt.clf()

    plt.hist(sat_list)
    plt.savefig("sat_score.png")
    plt.clf()


def plot_scatter():
    with open("admission_algorithms_dataset.csv", 'r') as infile:
        lines = infile.readlines()
        sat_list = []
        gpas = []
        for line in lines[1:]:
            line = line.strip('\n').split(',')
            sat, gpa = convert_row_type(line[1:3])
            sat_list.append(sat)
            gpas.append(gpa)

    plt.scatter(gpas, sat_list)
    plt.savefig("correlation.png")
    plt.clf()


def plot_spectra():
    """These are models of brown dwarfs, which are objects bigger than planets but not quite big enough to start
        hydrogen fusion in their cores and become stars. Both have surface temperatures of 1700 Kelvin (about 2600 degrees
        Fahrenheit). Spectrum 1 has no silicate clouds and spectrum 2 has fairly dense silicate clouds. The spectra look
        similar but there are differences in the wavelength where the flux is emitted because while they emit the same
        amount of energy, the clouds block light in some regions so the energy has to come out somewhere else."""
    with open("spectrum1.txt", 'r') as infile1:
        lines1 = infile1.readlines()
        waves1 = []
        fluxes1 = []
        for line in lines1:
            line = line.strip('\n').split('    ')
            wav, flux = convert_row_type(line)
            waves1.append(wav)
            fluxes1.append(flux)
    with open("spectrum2.txt", 'r') as infile2:
        lines2 = infile2.readlines()
        waves2 = []
        fluxes2 = []
        for line in lines2:
            line = line.strip('\n').split('    ')
            wav, flux = convert_row_type(line)
            waves2.append(wav)
            fluxes2.append(flux)
    plt.plot(waves1, fluxes1, 'b')
    plt.plot(waves2, fluxes2, 'g')

    # plt.title("Spectra")
    # plt.xlabel("Wavelength")
    # plt.ylabel("Flux")

    plt.savefig("spectra.png")
    plt.clf()


def main():
    # plot_histogram()
    # plot_scatter()
    # plot_spectra
    pass


if __name__ == "__main__":
    main()
