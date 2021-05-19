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
			output reg[DATA_WIDTH-1:0]	dat,
			output reg					valid,
			input						ready
		);
	
	reg[DATA_WIDTH-1:0]		data_v = 0;
	reg[1:0]				data_valid_v = 0;
	
	initial begin
		if (DATA_WIDTH > 64) begin
			$display("Error: rv_data_out_bfm %m -- DATA_WIDTH>64 (%0d)", DATA_WIDTH);
			$finish();
		end
	end
	
	reg[DATA_WIDTH-1:0]		trace_data = 0;
	reg						trace_active = 0;
	reg[31:0]				trace_id = 0;
	
	always @(posedge clock) begin
		if (reset) begin
			valid <= 0;
			dat <= 0;
		end else begin
			trace_active <= data_valid_v;
			
			if (data_valid_v > 0) begin
				trace_data <= data_v;
			end else begin
				trace_data <= {DATA_WIDTH{1'b0}};
			end
			if (valid && ready) begin
				data_valid_v = data_valid_v - 1;
				$display("ack");
				_send_ack();
				
				valid <= (data_valid_v > 0);
				dat <= data_v;
			end else begin
				valid <= (data_valid_v > 0);
				dat <= data_v;
			end
		end
	end
	
	task _send_req(input reg[63:0] d);
	begin
		$display("_send_req: 'h%h", d);
		data_v = d;
		data_valid_v = data_valid_v + 1;
		trace_id = trace_id + 1;
	end
	endtask
	

	task init;
		_set_parameters(DATA_WIDTH);
	endtask
	
	
	// Auto-generated code to implement the BFM API
`ifdef PYBFMS_GEN
${pybfms_api_impl}
`endif

endmodule

