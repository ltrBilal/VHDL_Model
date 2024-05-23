library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;
  
entity registre is
   port(
          clock : in std_logic;
          a : in unsigned(7 downto 0);
          res : out unsigned(8 downto 0)
   );
end registre;

architecture registre_arch of registre is
begin
      res <= a;
end registre_arch;