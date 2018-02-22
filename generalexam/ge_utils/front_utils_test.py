"""Unit tests for front_utils.py."""

import copy
import unittest
import numpy
from generalexam.ge_utils import front_utils

TOLERANCE = 1e-6

GRID_SPACING_X_METRES = 1.
GRID_SPACING_Y_METRES = 1.
ONE_GRID_POINT_X_METRES = 1.
ONE_GRID_POINT_Y_METRES = 2.
ONE_GRID_POINT_VERTEX_COORDS_X_METRES = numpy.array([0.5, 1.5, 1.5, 0.5, 0.5])
ONE_GRID_POINT_VERTEX_COORDS_Y_METRES = numpy.array([1.5, 1.5, 2.5, 2.5, 1.5])

POLYLINE_X_COORDS_METRES = numpy.array(
    [3.3, 2.3, 1.8, 1.5, 1.3, 1.4, 1.7, 2.1, 2.6, 2.8])
POLYLINE_Y_COORDS_METRES = numpy.array(
    [5.5, 4.7, 4.1, 3.5, 2.5, 1.5, 0.9, 0.1, -0.2, -0.5])
POLYLINE_VERTEX_LIST_XY_METRES = [
    (3.3, 5.5), (2.3, 4.7), (1.8, 4.1), (1.5, 3.5), (1.3, 2.5),
    (1.4, 1.5), (1.7, 0.9), (2.1, 0.1), (2.6, -0.2), (2.8, -0.5)]

NUM_GRID_ROWS = 6
NUM_GRID_COLUMNS = 8
GRID_POINT_X_COORDS_METRES = numpy.array([0., 1., 2., 3., 4., 5., 6., 7.])
GRID_POINT_Y_COORDS_METRES = numpy.array([0., 1., 2., 3., 4., 5.])

GRID_ROWS_IN_POLYLINE = numpy.array(
    [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5], dtype=int)
GRID_COLUMNS_IN_POLYLINE = numpy.array(
    [2, 3, 1, 2, 1, 1, 2, 1, 2, 2, 3], dtype=int)

POLYLINE_AS_BINARY_MATRIX = numpy.array([[0, 0, 1, 1, 0, 0, 0, 0],
                                         [0, 1, 1, 0, 0, 0, 0, 0],
                                         [0, 1, 0, 0, 0, 0, 0, 0],
                                         [0, 1, 1, 0, 0, 0, 0, 0],
                                         [0, 1, 1, 0, 0, 0, 0, 0],
                                         [0, 0, 1, 1, 0, 0, 0, 0]])

BINARY_MATRIX_DILATED_HW1_DIAGONAL_NO = numpy.array([[0, 1, 1, 1, 1, 0, 0, 0],
                                                     [1, 1, 1, 1, 0, 0, 0, 0],
                                                     [1, 1, 1, 0, 0, 0, 0, 0],
                                                     [1, 1, 1, 1, 0, 0, 0, 0],
                                                     [1, 1, 1, 1, 0, 0, 0, 0],
                                                     [0, 1, 1, 1, 1, 0, 0, 0]])

BINARY_MATRIX_DILATED_HW1_DIAGONAL_YES = numpy.array([[1, 1, 1, 1, 1, 0, 0, 0],
                                                      [1, 1, 1, 1, 1, 0, 0, 0],
                                                      [1, 1, 1, 1, 0, 0, 0, 0],
                                                      [1, 1, 1, 1, 0, 0, 0, 0],
                                                      [1, 1, 1, 1, 1, 0, 0, 0],
                                                      [1, 1, 1, 1, 1, 0, 0, 0]])

ROWS_IN_POLYLINE_DILATED_HALFWIDTH1 = numpy.array(
    [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],
    dtype=int)
COLUMNS_IN_POLYLINE_DILATED_HALFWIDTH1 = numpy.array(
    [1, 2, 3, 4, 0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 1, 2, 3, 4],
    dtype=int)

BINARY_MATRIX_DILATED_HW2_DIAGONAL_NO = numpy.array([[1, 1, 1, 1, 1, 1, 0, 0],
                                                     [1, 1, 1, 1, 1, 0, 0, 0],
                                                     [1, 1, 1, 1, 0, 0, 0, 0],
                                                     [1, 1, 1, 1, 1, 0, 0, 0],
                                                     [1, 1, 1, 1, 1, 0, 0, 0],
                                                     [1, 1, 1, 1, 1, 1, 0, 0]])

BINARY_MATRIX_DILATED_HW2_DIAGONAL_YES = numpy.array([[1, 1, 1, 1, 1, 1, 0, 0],
                                                      [1, 1, 1, 1, 1, 1, 0, 0],
                                                      [1, 1, 1, 1, 1, 1, 0, 0],
                                                      [1, 1, 1, 1, 1, 1, 0, 0],
                                                      [1, 1, 1, 1, 1, 1, 0, 0],
                                                      [1, 1, 1, 1, 1, 1, 0, 0]])

CLOSED_POLYLINE_LATITUDES_DEG = numpy.array([51.1, 53.5, 53.5, 51.1])
CLOSED_POLYLINE_LONGITUDES_DEG = numpy.array([246., 246.5, 246., 246.])
OPEN_POLYLINE_LATITUDES_DEG = copy.deepcopy(POLYLINE_Y_COORDS_METRES)
OPEN_POLYLINE_LONGITUDES_DEG = copy.deepcopy(POLYLINE_X_COORDS_METRES)

NUM_FRONTS = 2
WARM_FRONT_ROW_INDICES = numpy.array(
    [0, 0, 0, 0, 1, 1, 1, 1, 2, 2], dtype=int)
WARM_FRONT_COLUMN_INDICES = numpy.array(
    [1, 2, 3, 4, 0, 1, 2, 3, 1, 2], dtype=int)
COLD_FRONT_ROW_INDICES = numpy.array(
    [2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], dtype=int)
COLD_FRONT_COLUMN_INDICES = numpy.array(
    [0, 0, 1, 2, 3, 0, 1, 2, 3, 1, 2, 3, 4], dtype=int)

FRONTAL_GRID_DICT = {
    front_utils.WARM_FRONT_ROW_INDICES_COLUMN: WARM_FRONT_ROW_INDICES,
    front_utils.WARM_FRONT_COLUMN_INDICES_COLUMN: WARM_FRONT_COLUMN_INDICES,
    front_utils.COLD_FRONT_ROW_INDICES_COLUMN: COLD_FRONT_ROW_INDICES,
    front_utils.COLD_FRONT_COLUMN_INDICES_COLUMN: COLD_FRONT_COLUMN_INDICES
}

FRONTAL_GRID_MATRIX = numpy.array([[0, 1, 1, 1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 0, 0, 0, 0],
                                   [2, 1, 1, 0, 0, 0, 0, 0],
                                   [2, 2, 2, 2, 0, 0, 0, 0],
                                   [2, 2, 2, 2, 0, 0, 0, 0],
                                   [0, 2, 2, 2, 2, 0, 0, 0]])

UNCLOSED_FRONTAL_GRID_MATRIX = numpy.array([[0, 1, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 1, 1],
                                            [0, 0, 2, 2, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [2, 2, 2, 0, 0, 0, 0, 0]])

CLOSED_FRONTAL_GRID_MATRIX = numpy.array([[0, 1, 1, 0, 0, 0, 0, 0],
                                          [0, 0, 0, 1, 1, 1, 1, 1],
                                          [0, 0, 0, 0, 0, 0, 1, 1],
                                          [0, 0, 2, 2, 0, 0, 0, 0],
                                          [0, 0, 2, 0, 0, 0, 0, 0],
                                          [2, 2, 2, 0, 0, 0, 0, 0]])

# The following constants are used to test _get_thermal_advection_over_grid.
GRID_RELATIVE_U_WIND_MATRIX_M_S01 = numpy.array([[1., 1., -1., -1., -1., -1.],
                                                 [1., 1., -1., -1., 0., 0.],
                                                 [1., 1., -1., -1., 0., 0.],
                                                 [1., 1., -1., -1., 0., 0.]])
GRID_RELATIVE_V_WIND_MATRIX_M_S01 = numpy.array([[-1., -1., -1., -1., -1., -1.],
                                                 [-1., -1., 1., 1., 1., 1.],
                                                 [-1., -1., 1., 1., 1., 1.],
                                                 [-1., -1., 1., 1., 1., 1.]])
THERMAL_PARAM_MATRIX_KELVINS = numpy.array([[0., 5., 7., 9., 10., 10.],
                                            [0., 5., 15., 17., 18., 19.],
                                            [0., 5., 15., 17., 18., 19.],
                                            [0., 5., 15., 17., 18., 19.]])

X_ADVECTION_MATRIX_KELVINS_S01 = numpy.array([[-5., -3.5, 2., 1.5, 0.5, 0.],
                                              [-5., -7.5, 6., 1.5, 0., 0.],
                                              [-5., -7.5, 6., 1.5, 0., 0.],
                                              [-5., -7.5, 6., 1.5, 0., 0.]])
Y_ADVECTION_MATRIX_KELVINS_S01 = numpy.array([[0., 0., 8., 8., 8., 9.],
                                              [0., 0., -4., -4., -4., -4.5],
                                              [0., 0., 0., 0., 0., 0.],
                                              [0., 0., 0., 0., 0., 0.]])
ADVECTION_MATRIX_KELVINS_S01 = (
    X_ADVECTION_MATRIX_KELVINS_S01 + Y_ADVECTION_MATRIX_KELVINS_S01)

# The following constants are used to test get_frontal_types_over_grid.
BINARY_MATRIX_BEFORE_DISCRIMINATION = numpy.array(
    [[0, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0]], dtype=bool)
FRONTAL_GRID_MATRIX_AFTER_DISCRIMINATION = numpy.array(
    [[0, 0, 1, 1, 1, 1],
     [2, 2, 1, 0, 0, 0],
     [2, 2, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0]])


class FrontUtilsTests(unittest.TestCase):
    """Each method is a unit test for front_utils.py."""

    def test_vertex_arrays_to_list(self):
        """Ensures correct output from _vertex_arrays_to_list."""

        this_vertex_list_xy_metres = front_utils._vertex_arrays_to_list(
            vertex_x_coords_metres=POLYLINE_X_COORDS_METRES,
            vertex_y_coords_metres=POLYLINE_Y_COORDS_METRES)

        self.assertTrue(len(this_vertex_list_xy_metres) ==
                        len(POLYLINE_VERTEX_LIST_XY_METRES))

        for i in range(len(this_vertex_list_xy_metres)):
            self.assertTrue(numpy.allclose(
                this_vertex_list_xy_metres[i],
                POLYLINE_VERTEX_LIST_XY_METRES[i], atol=TOLERANCE))

    def test_grid_cell_to_polygon(self):
        """Ensures correct output from _grid_cell_to_polygon."""

        this_polygon_object_xy_metres = front_utils._grid_cell_to_polygon(
            grid_point_x_metres=ONE_GRID_POINT_X_METRES,
            grid_point_y_metres=ONE_GRID_POINT_Y_METRES,
            x_spacing_metres=GRID_SPACING_X_METRES,
            y_spacing_metres=GRID_SPACING_Y_METRES)

        these_vertex_x_metres = numpy.array(
            this_polygon_object_xy_metres.exterior.xy[0])
        these_vertex_y_metres = numpy.array(
            this_polygon_object_xy_metres.exterior.xy[1])

        self.assertTrue(numpy.allclose(
            these_vertex_x_metres, ONE_GRID_POINT_VERTEX_COORDS_X_METRES,
            atol=TOLERANCE))
        self.assertTrue(numpy.allclose(
            these_vertex_y_metres, ONE_GRID_POINT_VERTEX_COORDS_Y_METRES,
            atol=TOLERANCE))

    def test_polyline_to_grid_points(self):
        """Ensures correct output from _polyline_to_grid_points."""

        these_rows, these_columns = front_utils._polyline_to_grid_points(
            polyline_x_coords_metres=POLYLINE_X_COORDS_METRES,
            polyline_y_coords_metres=POLYLINE_Y_COORDS_METRES,
            grid_point_x_coords_metres=GRID_POINT_X_COORDS_METRES,
            grid_point_y_coords_metres=GRID_POINT_Y_COORDS_METRES)

        self.assertTrue(numpy.array_equal(these_rows, GRID_ROWS_IN_POLYLINE))
        self.assertTrue(numpy.array_equal(
            these_columns, GRID_COLUMNS_IN_POLYLINE))

    def test_grid_points_to_binary_image(self):
        """Ensures correct output from _grid_points_to_binary_image."""

        this_binary_matrix = front_utils._grid_points_to_binary_image(
            rows_in_object=GRID_ROWS_IN_POLYLINE,
            columns_in_object=GRID_COLUMNS_IN_POLYLINE,
            num_grid_rows=NUM_GRID_ROWS, num_grid_columns=NUM_GRID_COLUMNS)

        self.assertTrue(numpy.array_equal(
            this_binary_matrix, POLYLINE_AS_BINARY_MATRIX))

    def test_dilate_binary_image_halfwidth1_no_diagonal(self):
        """Ensures correct output from _dilate_binary_image.

        In this case, half-width of window = 1 grid cell and diagonal neighbours
        are *not* considered connected.
        """

        this_input_matrix = copy.deepcopy(POLYLINE_AS_BINARY_MATRIX)
        this_dilated_matrix = front_utils.dilate_binary_image(
            binary_matrix=this_input_matrix,
            dilation_half_width_in_grid_cells=1,
            include_diagonal_neighbours=False)

        self.assertTrue(numpy.array_equal(
            this_dilated_matrix, BINARY_MATRIX_DILATED_HW1_DIAGONAL_NO))

    def test_dilate_binary_image_halfwidth1_with_diagonal(self):
        """Ensures correct output from _dilate_binary_image.

        In this case, half-width of window = 1 grid cell and diagonal neighbours
        are considered connected.
        """

        this_input_matrix = copy.deepcopy(POLYLINE_AS_BINARY_MATRIX)
        this_dilated_matrix = front_utils.dilate_binary_image(
            binary_matrix=this_input_matrix,
            dilation_half_width_in_grid_cells=1,
            include_diagonal_neighbours=True)

        self.assertTrue(numpy.array_equal(
            this_dilated_matrix, BINARY_MATRIX_DILATED_HW1_DIAGONAL_YES))

    def test_dilate_binary_image_halfwidth2_no_diagonal(self):
        """Ensures correct output from _dilate_binary_image.

        In this case, half-width of window = 2 grid cell and diagonal neighbours
        are *not* considered connected.
        """

        this_input_matrix = copy.deepcopy(POLYLINE_AS_BINARY_MATRIX)
        this_dilated_matrix = front_utils.dilate_binary_image(
            binary_matrix=this_input_matrix,
            dilation_half_width_in_grid_cells=2,
            include_diagonal_neighbours=False)

        self.assertTrue(numpy.array_equal(
            this_dilated_matrix, BINARY_MATRIX_DILATED_HW2_DIAGONAL_NO))

    def test_dilate_binary_image_halfwidth2_with_diagonal(self):
        """Ensures correct output from _dilate_binary_image.

        In this case, half-width of window = 2 grid cell and diagonal neighbours
        are considered connected.
        """

        this_input_matrix = copy.deepcopy(POLYLINE_AS_BINARY_MATRIX)
        this_dilated_matrix = front_utils.dilate_binary_image(
            binary_matrix=this_input_matrix,
            dilation_half_width_in_grid_cells=2,
            include_diagonal_neighbours=True)

        self.assertTrue(numpy.array_equal(
            this_dilated_matrix, BINARY_MATRIX_DILATED_HW2_DIAGONAL_YES))

    def test_binary_image_to_grid_points(self):
        """Ensures correct output from _binary_image_to_grid_points."""

        these_rows, these_columns = front_utils._binary_image_to_grid_points(
            BINARY_MATRIX_DILATED_HW1_DIAGONAL_NO)

        self.assertTrue(numpy.array_equal(
            these_rows, ROWS_IN_POLYLINE_DILATED_HALFWIDTH1))
        self.assertTrue(numpy.array_equal(
            these_columns, COLUMNS_IN_POLYLINE_DILATED_HALFWIDTH1))

    def test_is_polyline_closed_yes(self):
        """Ensures correct output from _is_polyline_closed.

        In this case, the answer is yes.
        """

        self.assertTrue(front_utils._is_polyline_closed(
            vertex_latitudes_deg=CLOSED_POLYLINE_LATITUDES_DEG,
            vertex_longitudes_deg=CLOSED_POLYLINE_LONGITUDES_DEG))

    def test_is_polyline_closed_no(self):
        """Ensures correct output from _is_polyline_closed.

        In this case, the answer is no.
        """

        self.assertFalse(front_utils._is_polyline_closed(
            vertex_latitudes_deg=OPEN_POLYLINE_LATITUDES_DEG,
            vertex_longitudes_deg=OPEN_POLYLINE_LONGITUDES_DEG))

    def test_close_frontal_grid_matrix(self):
        """Ensures correct output from _close_frontal_grid_matrix."""

        this_input_matrix = copy.deepcopy(UNCLOSED_FRONTAL_GRID_MATRIX)
        this_closed_matrix = front_utils._close_frontal_grid_matrix(
            this_input_matrix)

        self.assertTrue(numpy.array_equal(
            this_closed_matrix, CLOSED_FRONTAL_GRID_MATRIX))

    def test_get_thermal_advection_over_grid(self):
        """Ensures correct output from _get_thermal_advection_over_grid."""

        this_advection_matrix_kelvins_s01 = (
            front_utils._get_thermal_advection_over_grid(
                grid_relative_u_wind_matrix_m_s01=
                GRID_RELATIVE_U_WIND_MATRIX_M_S01,
                grid_relative_v_wind_matrix_m_s01=
                GRID_RELATIVE_V_WIND_MATRIX_M_S01,
                thermal_param_matrix_kelvins=THERMAL_PARAM_MATRIX_KELVINS,
                grid_spacing_x_metres=GRID_SPACING_X_METRES,
                grid_spacing_y_metres=GRID_SPACING_Y_METRES))

        self.assertTrue(numpy.allclose(
            this_advection_matrix_kelvins_s01, ADVECTION_MATRIX_KELVINS_S01,
            atol=TOLERANCE))

    def test_frontal_grid_to_points(self):
        """Ensures correct output from frontal_grid_to_points."""

        this_frontal_grid_dict = front_utils.frontal_grid_to_points(
            FRONTAL_GRID_MATRIX)

        self.assertTrue(
            set(this_frontal_grid_dict.keys()) == set(FRONTAL_GRID_DICT.keys()))

        for this_key in FRONTAL_GRID_DICT.keys():
            self.assertTrue(numpy.array_equal(
                this_frontal_grid_dict[this_key], FRONTAL_GRID_DICT[this_key]))

    def test_frontal_points_to_grid(self):
        """Ensures correct output from frontal_points_to_grid."""

        this_frontal_grid_matrix = front_utils.frontal_points_to_grid(
            frontal_grid_dict=FRONTAL_GRID_DICT, num_grid_rows=NUM_GRID_ROWS,
            num_grid_columns=NUM_GRID_COLUMNS)

        self.assertTrue(numpy.array_equal(
            this_frontal_grid_matrix, FRONTAL_GRID_MATRIX))

    def test_frontal_grid_to_regions(self):
        """Ensures correct output from frontal_grid_to_regions."""

        this_input_matrix = copy.deepcopy(FRONTAL_GRID_MATRIX)
        this_frontal_region_dict = front_utils.frontal_grid_to_regions(
            this_input_matrix)

        this_num_fronts = len(
            this_frontal_region_dict[front_utils.FRONT_TYPE_BY_REGION_KEY])
        self.assertTrue(this_num_fronts == NUM_FRONTS)

        for i in range(NUM_FRONTS):
            this_front_type_string = this_frontal_region_dict[
                front_utils.FRONT_TYPE_BY_REGION_KEY][i]

            if this_front_type_string == front_utils.WARM_FRONT_STRING_ID:
                self.assertTrue(numpy.array_equal(
                    this_frontal_region_dict[
                        front_utils.ROW_INDICES_BY_REGION_KEY][i],
                    WARM_FRONT_ROW_INDICES))
                self.assertTrue(numpy.array_equal(
                    this_frontal_region_dict[
                        front_utils.COLUMN_INDICES_BY_REGION_KEY][i],
                    WARM_FRONT_COLUMN_INDICES))

            else:
                self.assertTrue(numpy.array_equal(
                    this_frontal_region_dict[
                        front_utils.ROW_INDICES_BY_REGION_KEY][i],
                    COLD_FRONT_ROW_INDICES))
                self.assertTrue(numpy.array_equal(
                    this_frontal_region_dict[
                        front_utils.COLUMN_INDICES_BY_REGION_KEY][i],
                    COLD_FRONT_COLUMN_INDICES))

    def test_get_frontal_types_over_grid(self):
        """Ensures correct output from get_frontal_types_over_grid."""

        this_frontal_grid_matrix = front_utils.get_frontal_types_over_grid(
            grid_relative_u_wind_matrix_m_s01=GRID_RELATIVE_U_WIND_MATRIX_M_S01,
            grid_relative_v_wind_matrix_m_s01=GRID_RELATIVE_V_WIND_MATRIX_M_S01,
            thermal_param_matrix_kelvins=THERMAL_PARAM_MATRIX_KELVINS,
            binary_matrix=BINARY_MATRIX_BEFORE_DISCRIMINATION,
            grid_spacing_x_metres=GRID_SPACING_X_METRES,
            grid_spacing_y_metres=GRID_SPACING_Y_METRES)

        self.assertTrue(numpy.array_equal(
            this_frontal_grid_matrix, FRONTAL_GRID_MATRIX_AFTER_DISCRIMINATION))


if __name__ == '__main__':
    unittest.main()