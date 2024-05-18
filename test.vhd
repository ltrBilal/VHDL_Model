library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;

entity test is
   port(
          clk : in std_logic;
          a : in unsigned(7 downto 0);
          b : in unsigned(7 downto 0);
          c : in unsigned(7 downto 0);
          res : out unsigned(8 downto 0)
   );
end test;

architecture test_arch of test is
      signal res_int : unsigned(7 downto 0); 
begin

-- instantiate an adder
   first_adder: entity work.adder(adder_arch)
    port map(
       clk => clk,
       a => a,
       b => b,
       res => res_int
    );

-- instantiate an adder
   second_adder: entity work.adder(adder_arch)
    port map(
       clk => clk,
       a => c,
       b => res_int,
       res => res
    );
   clock_process : process
   begin
      clk <= '0';
      wait for 10 ns;
      clk <= '1';
      wait for 10 ns;
   end process;
end test_arch;
