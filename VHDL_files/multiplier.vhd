library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;
  
entity multiplier is
   port(
          clock : in std_logic;
          a : in unsigned(15 downto 0);
          b : in unsigned(15 downto 0);
          res : out unsigned(31 downto 0)
   );
end multiplier;

architecture multiplier_arch of multiplier is
begin
      res <= ('0' & a) * ('0' & b);
end multiplier_arch;