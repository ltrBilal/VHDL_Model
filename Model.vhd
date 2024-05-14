library ieee;
use ieee.std_logic_1164.all;
use ieee.NUMERIC_STD.all;

entity test is

end test;

architecture test_arch of test is
begin

    -- instanciation for adder
   first_adder: entity work.adder(adder_arch)
    port map(
       clock => clock,
       a => a,
       b => b,
       res => res
    );

    -- instanciation for adder
   second_adder: entity work.adder(adder_arch)
    port map(
       clock => clock,
       a => a,
       b => b,
       res => res
    );
end test_arch;
