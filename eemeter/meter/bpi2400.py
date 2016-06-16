from eemeter.meter.base import YamlDefinedMeter


with open('bpi2400.yaml', 'r') as f:
    bpi_meter_yaml = f.read()


class BPI_2400_S_2012_ModelCalibrationUtilityBillCriteria(YamlDefinedMeter):
    """Implementation of BPI-2400-S-2012 section 3.2.2.

    Parameters
    ----------
    temperature_unit_str : {"degF", "degC"}, default "degC"
        Temperature unit to use throughout meter in degree-day calculations and
        parameter optimizations.
    settings : dict
        - electricity_baseload_low (float):
          Lowest baseload in parameter optimization for electricity;
          defaults to 0 energy units/day
        - electricity_baseload_x0 (float):
          Initial baseload in parameter optimization for electricity;
          defaults to 0 energy units/day
        - electricity_baseload_high (float):
          Highest baseload in parameter optimization for electricity;
          defaults to 1000 energy units/day


        - electricity_heating_slope_low (float):
          Lowest heating slope in parameter optimization for electricity;
          defaults to 0 energy units/degF/day
        - electricity_heating_slope_x0 (float):
          Initial heating slope in parameter optimization for electricity;
          defaults to 0 energy units/degF/day
        - electricity_heating_slope_high (float):
          Highest heating slope in parameter optimization for electricity;
          defaults to or 100 energy units/degF/day

        - electricity_cooling_slope_low (float):
          Lowest cooling slope in parameter optimization for electricity;
          defaults to 0 energy units/degF/day
        - electricity_cooling_slope_x0 (float):
          Initial cooling slope in parameter optimization for electricity;
          defaults to 0 energy units/degF/day
        - electricity_cooling_slope_high (float):
          Highest cooling slope in parameter optimization for electricity;
          defaults to 100 energy units/degF/day


        - natural_gas_baseload_low (float):
          Lowest baseload in parameter optimization for natural gas;
          defaults to 0 energy units/day
        - natural_gas_baseload_x0 (float):
          Initial baseload in parameter optimization for natural gas;
          defaults to 0 energy units/day
        - natural_gas_baseload_high (float):
          Highest baseload in parameter optimization for natural gas;
          defaults to 1000 energy units/day

        - natural_gas_heating_slope_low (float):
          Lowest heating slope in parameter optimization for natural gas;
          defaults to 0 energy units/degF/day
        - natural_gas_heating_slope_x0 (float):
          Initial heating slope in parameter optimization for natural gas;
          defaults to 0 energy units/degF/day
        - natural_gas_heating_slope_high (float):
          Highest heating slope in parameter optimization for natural gas;
          defaults to 100 energy units/degF/day

        - heating_balance_temp_low (float):
          Lowest heating balance temperature in parameter optimization;
          defaults to 55 degF
        - heating_balance_temp_x0 (float):
          Initial heating balance temperature in parameter optimization;
          defaults to 60 degF
        - heating_balance_temp_high (float):
          Highest heating balance temperature in parameter optimization;
          defaults to 70 degF
        - cooling_balance_temp_low (float):
          Lowest cooling balance temperature in parameter optimization;
          defaults to 60 degF
        - cooling_balance_temp_x0 (float):
          Initial cooling balance temperature in parameter optimization;
          defaults to 70 degF
        - cooling_balance_temp_high (float):
          Highest cooling balance temperature in parameter optimization;
          defaults to 75 degF

        - hdd_base (float):
          Base for Heating Degree Day calculations.
          defaults to 65 degF
        - cdd_base (float):
          Base for Cooling Degree Day calculations.
          defaults to 65 degF
    """

    def __init__(self, temperature_unit_str, **kwargs):
        if temperature_unit_str not in ["degF", "degC"]:
            error = ("Invalid temperature_unit_str: should be one of 'degF' "
                     "or 'degC'.")
            raise ValueError(error)

        self.temperature_unit_str = temperature_unit_str

        super(BPI_2400_S_2012_ModelCalibrationUtilityBillCriteria,
              self).__init__(**kwargs)

    def default_settings(self):

        def degF_to_degC(F):
            return (F - 32.) * 5. / 9.

        def temp_degF_to_target(temp_degF):
            if self.temperature_unit_str == "degF":
                return temp_degF
            else:
                return degF_to_degC(temp_degF)

        def slope_degF_to_target(slope_degF):
            if self.temperature_unit_str == "degF":
                return slope_degF
            else:
                return slope_degF * 1.8

        settings = {
            "temperature_unit_str": self.temperature_unit_str,
            "electricity_baseload_low": 0,
            "electricity_baseload_x0": 0,
            "electricity_baseload_high": 1000,
            "electricity_heating_slope_low": slope_degF_to_target(0),
            "electricity_heating_slope_x0": slope_degF_to_target(0),
            "electricity_heating_slope_high": slope_degF_to_target(1000),
            "electricity_cooling_slope_low": slope_degF_to_target(0),
            "electricity_cooling_slope_x0": slope_degF_to_target(0),
            "electricity_cooling_slope_high": slope_degF_to_target(1000),

            "natural_gas_baseload_low": 0,
            "natural_gas_baseload_x0": 0,
            "natural_gas_baseload_high": 1000,
            "natural_gas_heating_slope_low": slope_degF_to_target(0),
            "natural_gas_heating_slope_x0": slope_degF_to_target(0),
            "natural_gas_heating_slope_high": slope_degF_to_target(1000),

            "heating_balance_temp_low": temp_degF_to_target(55),
            "heating_balance_temp_x0": temp_degF_to_target(60),
            "heating_balance_temp_high": temp_degF_to_target(70),
            "cooling_balance_temp_low": temp_degF_to_target(60),
            "cooling_balance_temp_x0": temp_degF_to_target(70),
            "cooling_balance_temp_high": temp_degF_to_target(75),

            "hdd_base": temp_degF_to_target(65),
            "cdd_base": temp_degF_to_target(65),
        }
        return settings

    def validate_settings(self, settings):
        groups = (('electricity_baseload', 'Electricity baseload'),
                  ('electricity_heating_slope', 'Electricity heating slope'),
                  ('electricity_cooling_slope', 'Electricity cooling slope'),
                  ('natural_gas_baseload', 'Natural gas baseload'),
                  ('natural_gas_heating_slope', 'Electricity heating slope'),
                  ('heating_balance_temp', 'Heating balance temperature'),
                  ('cooling_balance_temp', 'Cooling balance temperature'))

        for partial_key, parameter_type in groups:
            low = settings['{}_low'.format(partial_key)]
            high = settings['{}_high'.format(partial_key)]
            x0 = settings['{}_x0'.format(partial_key)]

            if not 0 <= low <= x0 <= high:
                error = ("{} parameter limits must be such "
                         "that 0 <= low <= x0 <= high, "
                         "but found low={}, x0={}, high={}")

                raise ValueError(error.format(parameter_type, low, x0, high))

    @property
    def yaml(self):
        return bpi_meter_yaml

    def evaluate(self, data_collection):
        """Evaluates utility bills for compliance with criteria specified in
        ANSI/BPI-2400-S-2012 section 3.2.2.

        Parameters
        ----------
        consumption_history : eemeter.consumption.ConsumptionHistory
            All available billing data (of all fuel types) available for the
            target project. Estimated bills must be flagged.
        weather_source : eemeter.weather.WeatherSourceBase
            Weather data should come from a source as geographically and
            climatically similar to the target project as possible.
        weather_normal_source : eemeter.weather.WeatherSourceBase with
            eemeter.weather.WeatherNormalMixin
            Weather normal data should come from a source as geographically and
            climatically similar to the target project as possible.
        since_date : datetime.datetime, optional
            The date from which to count days since most recent reading;
            defaults to datetime.now(pytz.utc).

        Returns
        -------
        out : eemeter.meter.DataCollection

            - *"average_daily_usages_bpi2400"* : Average usage per
              day (kWh/day) for the consumption periods.
            - *"cdd_tmy"* : Total cooling degree days (base 65 degF or
              18.33 degC) in a typical meteorological year (TMY3).
            - *"consumption_history_no_estimated"* : The input consumption
              history with estimated periods consolidated or removed.
            - *"cvrmse"* : The Coefficient of Variation of
              Root-mean-squared Error on the outputs of the usage model.
            - *"estimated_average_daily_usages"* : Average usage per day for
              the consumption_periods as estimated by the fitted temperature
              sensitivity model.
            - *"has_enough_cdd"* : A boolean indicating whether or not
              the consumption data covers (a) enough total CDD, (b)
              enough periods with low CDD, and (c) enough periods with high
              CDD.
            - *"has_enough_data"* : A boolean indicating whether or not
              the consumption data covers a period of at least 330
              days or a period of at least 184 days with enough CDD and HDD
              variation, as indicated by the results "has_enough_cdd" and
              "has_enough_hdd".
            - *"has_enough_data"* : A boolean indicating whether or not
              the consumption data covers a period of at least 330
              days or a period of at least 184 days with enough CDD and HDD
              variation, as indicated by the result "has_enough_hdd_cdd".
            - *"has_enough_hdd_cdd"* : A boolean indicating whether or
              not the electricity consumption data covers a period with enough
              variation in hdd and cdd; equivalent to the boolean value
              ("has_enough_cdd" and "has_enough_hdd").
            - *"has_enough_hdd"* : A boolean indicating whether or not
              the consumption data covers (a) enough total HDD, (b)
              enough periods with low HDD, and (c) enough periods with high
              HDD.
            - *"has_enough_periods_with_high_cdd_per_day"* : A boolean
              indicating whether or not the consumption data has
              enough periods with at least 1.2x average normal CDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_enough_periods_with_high_hdd_per_day"* : A boolean
              indicating whether or not the consumption data has
              enough periods with at least 1.2x average normal HDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_enough_periods_with_low_cdd_per_day"* : A boolean
              indicating whether or not the consumption data has
              enough periods with less than 0.2x average normal CDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_enough_periods_with_low_hdd_per_day"* : A boolean
              indicating whether or not the consumption data has
              enough periods with less than 0.2x average normal HDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_enough_total_cdd"* : A boolean indicating whether
              or not the total CDD during the total time span of the
              data is at least 0.5x normal annual CDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_enough_total_hdd"* : A boolean indicating whether
              or not the total HDD during the total time span of the
              data is at least 0.5x normal annual HDD/day (TMY3,
              base 65 degF or 18.33 degC).
            - *"has_recent_reading"* : A boolean indicating whether or
              not there is valid (not missing) consumption data within 365 days
              of the last date in the consumption data.
            - *"hdd_tmy"* : Total heating degree days (base 65 degF or
              18.33 degC) in a typical meteorological year (TMY3).
            - *"meets_cvrmse_limit"* : A boolean indicating whether or
              not the Coefficient of Variation of the Root-mean-square Error
              (CVRMSE) of a regression of consumption data against
              local observed HDD/CDD, as determined using equation 3.2.2.G.i
              of the ANSI/BPI-2400-S-2012 specification is less than 20.
            - *"meets_model_calibration_utility_bill_criteria"* : A
              boolean indicating whether or not consumption data
              acceptance criteria, as outlined in section 3.2.2 of the
              ANSI/BPI-2400-S-2012 specification, have been met.
            - *"n_periods_high_cdd_per_day"* : The number of
              consumption data periods with observed CDD greater
              than 1.2x average normal CDD/day (TMY3, base 65 degF or 18.33
              degC).
            - *"n_periods_low_cdd_per_day"* : The number of
              consumption data periods with observed CDD less than
              0.2x average normal CDD/day (TMY3, base 65 degF or 18.33 degC).
            - *"n_periods_low_hdd_per_day"* : The number of
              consumption data periods with observed HDD less than
              0.2x average normal CDD/day (TMY3, base 65 degF or 18.33 degC).
            - *"n_periods_high_cdd_per_day"* : The number of natural
              consumption data periods with observed CDD greater than 1.2x
              average normal CDD/day (TMY3, base 65 degF or 18.33 degC).
            - *"n_periods_high_hdd_per_day"* : The number of natural
              consumption data periods with observed HDD greater than 1.2x
              average normal CDD/day (TMY3, base 65 degF or 18.33 degC).
            - *"spans_183_days_and_has_enough_hdd_cdd"* : A boolean
              indicating whether or not consumption data spans at
              least 184 days and is associated with sufficient breadth and
              variation in observed HDD and CDD.
            - *"spans_184_days"* : A boolean indicating whether or not
              consumption data spans at least 184 days.
            - *"spans_330_days"* : A boolean indicating whether or not
              consumption data spans at least 330 days.
            - *"model_params"* : Fitted temperature
              sensitivity parameters for HDD/CDD use model in an
              array of values with the following order:

              For electricty: [base_daily_consumption (kWh/day),
              heating_balance_temperature (degF or degC),
              heating_slope (kWh/HDD),
              cooling_balance_temperature (degF or degC),
              cooling_slope (kWh/CDD)].

              For natural_gas: [base_daily_consumption (kWh/day),
              heating_balance_temperature (degF or degC),
              heating_slope (kWh/HDD)].

            - *"time_span"* : Number of days between earliest available
              data and latest available data.
            - *"total_cdd"* : The total cooling degree days (base 65
              degF or 18.33 degC) observed during the all consumption data
              periods.
            - *"total_hdd"* : The total heating degree days (base 65
              degF or 18.33 degC) observed during the all consumption data
              periods.

        """
        return super(
            BPI_2400_S_2012_ModelCalibrationUtilityBillCriteria,
            self).evaluate(data_collection)
