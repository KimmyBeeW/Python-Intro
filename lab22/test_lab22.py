from byu_pytest_utils import max_score, this_folder, test_files, with_import, ensure_missing
from byuimage import Image
from pytest import approx


def assert_equal(observed: Image, expected: Image):
    assert observed.width == expected.width
    assert observed.height == expected.height
    for y in range(observed.height):
        for x in range(observed.width):
            observed_pixel = observed.get_pixel(x, y)
            expected_pixel = expected.get_pixel(x, y)
            assert observed_pixel.red == approx(expected_pixel.red, abs=1.1), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel.red}`, but got `{observed_pixel.red}`."
            assert observed_pixel.green == approx(expected_pixel.green, abs=1.1), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel.green}`, but got `{observed_pixel.green}`."
            assert observed_pixel.blue == approx(expected_pixel.blue, abs=1.1), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel.blue}`, but got `{observed_pixel.blue}`."


@max_score(6)
@with_import('lab22', 'plot_histogram')
@ensure_missing(this_folder / 'sat_score.png')
@ensure_missing(this_folder / 'gpa.png')
def test_plot_histogram(plot_histogram):
    sat_key = Image(test_files / 'sat_score.key.png')
    gpa_key = Image(test_files / 'gpa.key.png')

    plot_histogram()

    sat_observed = Image('sat_score.png')
    gpa_observed = Image('gpa.png')

    assert_equal(sat_observed, sat_key)
    assert_equal(gpa_observed, gpa_key)


@max_score(6)
@with_import('lab22', 'plot_scatter')
@ensure_missing(this_folder / 'correlation.png')
def test_plot_scatter(plot_scatter):
    correlation_key = Image(test_files / 'correlation.key.png')
    plot_scatter()
    correlation_observed = Image('correlation.png')
    assert_equal(correlation_observed, correlation_key)


@max_score(8)
@with_import('lab22', 'plot_spectra')
@ensure_missing(this_folder / 'spectra.png')
def test_plot_spectra(plot_spectra):
    spectra_key = Image(test_files / 'spectra.key.png')
    plot_spectra()
    spectra_observed = Image('spectra.png')
    assert_equal(spectra_observed, spectra_key)
