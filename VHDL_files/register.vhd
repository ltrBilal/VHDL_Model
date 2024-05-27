library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;
  
entity register is
   port(
          clock : in std_logic;
          a : in unsigned(15 downto 0);
          res : out unsigned(31 downto 0)
   );
end register;

architecture register_arch of register is
begin
      res <= a;
end register_arch;