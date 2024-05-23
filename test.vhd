library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;

entity test is
   port(
          clock : in std_logic;
          a : in unsigned(7 downto 0);
          b : in unsigned(7 downto 0);
          c : in unsigned(7 downto 0);
          res : out unsigned(8 downto 0)
   );
end test;

architecture test_arch of test is
      signal res_int : unsigned(7 downto 0); 
      signal clock_tb : std_logic; 
begin

-- instantiate an adder
   first_adder: entity work.adder(adder_arch)
    port map(
       clock => clock,
       a => a,
       b => b,
       res => res_int
    );

-- instantiate an adder
   second_adder: entity work.adder(adder_arch)
    port map(
       clock => clock,
       a => c,
       b => res_int,
       res => res
    );

-- instantiate an registre
   reg1: entity work.registre(registre_arch)
    port map(
       clock => clock,
       a => a,
       res => res
    );
   -- clock simulation
   clock_process : process
   begin
      clock_tb <= '0';
      wait for 10 ns;
      clock_tb <= '1';
      wait for 10 ns;
   end process;

    -- p1 process
   p1 : process (clock,a,b)
   begin
       wait;
   end process;

end test_arch;
