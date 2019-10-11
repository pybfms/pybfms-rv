/****************************************************************************
 * rv_data_out_bfm.sv
 ****************************************************************************/

/**
 * Module: rv_data_out_bfm
 * 
 * TODO: Add module documentation
 */
module rv_data_out_bfm #(
		parameter DATA_WIDTH = 8
		) (
			input						clock,
			input						reset,
			output[DATA_WIDTH-1:0]		data,
			output						data_valid,
			input						data_ready
		);

endmodule


