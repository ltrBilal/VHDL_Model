library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;
  
entity adder is
   port(
          clk : in std_logic;
          a : in unsigned(7 downto 0);
          b : in unsigned(7 downto 0);
          res : out unsigned(8 downto 0)
   );
end adder;

architecture adder_arch of adder is
begin
      res <= ('0' & a) + ('0' & b);
end adder_arch;