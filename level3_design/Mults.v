module mult(eqz, ldA, ldB, ldP, clrP, decB, data_in, clk, done, start);
inout eqz;
inout reg ldA, ldB, ldP, clrP, decB;
input clk, start;
input [15:0]data_in;
output reg done;

controller C(ldA, ldB, ldP, clrP, decB, done, clk, eqz, start);
MUL_datapath M(eqz, ldA, ldB, ldP, clrP, decB, data_in, clk);

endmodule

