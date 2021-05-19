/****************************************************************************
 * rv_data_in_bfm.sv
 ****************************************************************************/

/**
 * Module: rv_data_in_bfm
 * 
 * TODO: Add module documentation
 */
module rv_data_in_bfm #(
		parameter DATA_WIDTH = 8
		) (
			input						clock,
			input						reset,
			input[DATA_WIDTH-1:0]		dat,
			input						valid,
			output						ready
		);

	// Should improve at some point
	reg ready_r = 1;
	assign ready = ready_r;

	reg in_reset = 0;
	always @(posedge clock or posedge reset) begin
		if (reset) begin
			in_reset <= 1;
		end else begin
			if (in_reset) begin
				_reset();
				in_reset <= 0;
			end
			if (valid && ready) begin
				_recv(dat);
			end
		end
	end
	
	task init;
		_set_parameters(DATA_WIDTH);
	endtask
	
	// Auto-generated code to implement the BFM API
`ifdef PYBFMS_GEN
${pybfms_api_impl}
`endif

endmodule


