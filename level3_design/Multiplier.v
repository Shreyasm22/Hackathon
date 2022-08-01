//Datapath

module MUL_datapath(eqz, ldA, ldB, ldP, clrP, decB, data_in, clk);
    input ldA, ldB, ldP, clrP, decB, clk;
    input [15:0] data_in;
    output eqz;
    wire [15:0] x,y,z,bout,bus;

    assign bus = data_in;

    PIPO1 A(x, bus, ldA, clk);
    PIPO2 B(y, z, ldP, clrP, clk);
    CNTR C(bout, bus, ldB, decB, clk);
    ADD D(z, x, y);
    EQZ E(eqz, bout);

endmodule

//PIPO1

module PIPO1(dout, din, ld, clk);
    input [15:0] din;
    input ld,clk;
    output reg [15:0] dout;

    always@(posedge clk)
        if(ld) dout <= din;

endmodule

//PIPO2

module PIPO2(dout, din, ld, clr, clk);
    input [15:0] din;
    input ld, clr, clk;
    output reg [15:0] dout;

    always@(posedge clk)
        if(clr) dout <= 16'b0;
        else if(ld) dout <= din; 
endmodule

//ADD

module ADD(out, in1, in2);
    input [15:0] in1, in2;
    output reg [15:0] out;

    always@(*)
        out = in1 + in2;
endmodule

//EQZ

module EQZ(eqz, data);
    input [15:0] data;
    output eqz;

    assign eqz = (data == 0);

endmodule

//CNTR

module CNTR(dout, din, ld, dec, clk);
    input [15:0] din;
    input ld, dec, clk;
    output reg [15:0] dout;

    always@(posedge clk)
        if(ld) dout <= din;
        else if(dec && dout != 0) dout <= dout - 2;
endmodule

//Controlpath

module controller(ldA, ldB, ldP, clrP, decB, done, clk, eqz);
    input clk, eqz;
    output reg ldA, ldB, ldP, clrP, decB, done;
    reg [2:0] state;
    parameter S0 = 3'b000, S1 = 3'b001, S2 = 3'b010, S3 = 3'b011, S4 = 3'b100;

    always@(posedge clk)
    begin
        case(state)

            S0 : state <= S1;
            S1 : state <= S2;
            S2 : state <= S3;
            S3 : #2 if(eqz) state <= S4;
            S4 : state <= S4;

            default : state <= S0;

        endcase

    end 

    always@(state)
    begin

        case(state)

            S0 : begin #1 ldA = 0; ldB = 0; ldP = 0; clrP = 0; decB = 0; done = 0; end
            S1 : begin #1 ldA = 1; end
            S2 : begin #1 ldA = 0; ldB = 1; clrP = 1; end
            S3 : begin #1 ldB = 0; ldP = 1; clrP = 0; decB = 1; end
            S4 : begin #8 done = 1; ldB = 0; ldP = 0; decB = 0; end

            default : begin #1 ldA = 0; ldB = 0; ldP = 0; clrP = 0; decB = 0; end

        endcase 

    end

endmodule

 