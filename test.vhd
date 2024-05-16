library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;

entity test is
   port(
          clk : in std_logic;
          a : in unsigned(7 downto 0);
          b : in unsigned(7 downto 0);
          res : out unsigned(8 downto 0)
   );
end test;

architecture test_arch of test is
      signal k_int : unsigned(7 downto 0); 
begin

-- instantiate an adder
   first_adder: entity work.adder(adder_arch)
    port map(
       clk => clk,
       a => k_int,
       b => b,
       res => res
    );

end test_arch;
