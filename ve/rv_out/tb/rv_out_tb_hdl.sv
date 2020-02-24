/****************************************************************************
 * rv_out_tb_hdl.sv
 ***************************************************************************/
 
`ifdef IVERILOG
`timescale 1ns/1ns
`endif

module rv_out_tb_hdl(
	input clock /*verilator public */
	);

`ifdef HAVE_HDL_CLKGEN
	reg clk_r = 0;

	initial begin
		forever begin
			#10ns;
			clk_r <= ~clk_r;
		end
	end

	assign clock = clk_r;
`endif

	reg reset = 1;
	reg [7:0] reset_cnt = 0;

	always @(posedge clock) begin
		if (reset_cnt == 10) begin
			reset <= 0;
		end else begin
			reset_cnt <= reset_cnt + 1;
		end
	end
	
	wire[31:0]			data;
	wire				data_valid;
	wire				data_ready;
	
	rv_data_out_bfm #(32) u_dut (
			.clock(clock),
			.reset(reset),
			.data(data),
			.data_valid(data_valid),
			.data_ready(data_ready)
		);
	
	rv_data_monitor_bfm #(32) u_mon (
			.clock(clock),
			.reset(reset),
			.data(data),
			.data_valid(data_valid),
			.data_ready(data_ready)
		);

	reg[7:0]			delay_count;
	reg[1:0]			state;
	assign data_ready = (state == 1 && delay_count == 0);
	
	always @(posedge clock) begin
		if (reset) begin
			delay_count <= 0;
			state <= 0;
		end else begin
			case (state)
				0: begin
					if (data_valid) begin
						delay_count <= ($random % 32);
						state <= 1;
					end
				end
				1: begin
					if (delay_count == 0) begin
						state <= 0;
					end else begin
						delay_count <= delay_count - 1;
					end
				end
			endcase
		end
	end
	

	
endmodule
