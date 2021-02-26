/****************************************************************************
 * rv_addr_line_en_initiator_bfm.v
 * 
 ****************************************************************************/

module rv_addr_line_en_initiator_bfm #(
		parameter ADR_WIDTH = 32,
		parameter DAT_WIDTH = 32
        ) (
        input							clock,
        input							reset,
        output[ADR_WIDTH-1:0]			adr,
        output[DAT_WIDTH-1:0]			dat_w,
        input[DAT_WIDTH-1:0]			dat_r,
        output							we,
        output							valid,
        input							ready);
    reg						in_reset = 0;
    reg[ADR_WIDTH-1:0]		adr_r = {ADR_WIDTH{1'b0}};
    reg[ADR_WIDTH-1:0]		adr_v = {ADR_WIDTH{1'b0}};
    reg[DAT_WIDTH-1:0]		dat_w_r = {DAT_WIDTH{1'b0}};
    reg[DAT_WIDTH-1:0]		dat_w_v = {DAT_WIDTH{1'b0}};
    reg						we_r = 1'b0;
    reg						we_v = 1'b0;
    reg[1:0]				valid_v = 2'b00;
    reg						valid_r = 0;
    
    assign valid = valid_r;
    assign adr = adr_r;
    assign dat_w = dat_w_r;
    assign we = we_r;
    
    reg state = 0;
    
    always @(posedge clock or posedge reset) begin
        if (reset) begin
            in_reset <= 1;
            state <= 0;
        end else begin
            if (in_reset) begin
                _reset();
                in_reset <= 1'b0;
            end
            
       		if (valid && ready) begin
       			valid_v = (valid_v-1);
       			we_v = 0;
       			adr_v = {ADR_WIDTH{1'b0}};
       			dat_w_v = {DAT_WIDTH{1'b0}};
       			_access_ack(dat_r);
       			valid_r <= |valid_v;
       			adr_r <= adr_v;
       			we_r <= we_v;
            	dat_w_r <= dat_w_v;
      			state <= 0;
       		end else begin
       			valid_r <= |valid_v;
       			adr_r <= adr_v;
       			we_r <= we_v;
            	dat_w_r <= dat_w_v;
       		end
       		/*
            case (state) 
            	0: begin
            		if (valid_r) begin
            			state <= 1;
            		end
            	end
            	1: begin
            	end
            endcase
             */
        end
    end
    
    task _access_req(
    	input[63:0] 	adr,
    	input[63:0]		dat_w,
    	input[7:0]		we);
   	begin
   		valid_v = valid_v + 1;
   		adr_v = adr;
   		dat_w_v = dat_w;
   		we_v = we;
   	end
    endtask
        
    task init;
    begin
        $display("rv_addr_line_en_initiator_bfm: %m");
        _set_parameters(ADR_WIDTH, DAT_WIDTH);
    end
    endtask
	
    // Auto-generated code to implement the BFM API
`ifdef PYBFMS_GEN
${pybfms_api_impl}
`endif

endmodule
