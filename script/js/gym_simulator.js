import * as sim from "./simulator_class.js"
import * as cnct from "./fb_connect.js"

/** 
 * @param {sim.Exercise_Params} handle 
 */
function simulation_process(handle) {
  handle.reset_all_params();

  handle.read_preset();
  handle.read_params();

  handle.initialize();
  handle.show_basic_info();
  handle.iter_process();
  handle.render_result();
}

/** 
 * @param {sim.Exercise_Params} handle 
 */
function watch_btn(handle) {
  var startButton = cnct.get_start_btn();
  startButton.addEventListener('click', function () {
    console.log("Start Simulation!");
    simulation_process(handle);
  });

  var resetButton = cnct.get_reset_btn();
  resetButton.addEventListener('click', function () {
    console.log("Reset Simulation Params!");
    handle.reset_all_params();
    cnct.get_all_gym_row().forEach( element => {
      if (cnct.get_attr_select(element).length > 5)
        cnct.get_attr_select(element).selectedIndex = 5;
      else
        cnct.get_attr_select(element).selectedIndex = 0;
    });
  });
}

/** 
 * @param {sim.Exercise_Params} handle 
 */
function watch_preset(handle) {
  var presetOpt = cnct.get_preset_select();

  presetOpt.onchange = function () {
    handle.get_start_stop_gym();
    handle.get_initial_stats();
    if (this.selectedIndex == sim.PRESET_SELECTOR_USER_DEFINED) {
      return;
    }
    else {
      cnct.get_all_gym_row().forEach( element => {
        cnct.get_attr_select(element).selectedIndex = 4;
      });
    }
  };
}

/**
 * @param {sim.Exercise_Params} handle
 */
function watch_dots(handle) {
  cnct.get_all_attr_select().forEach(element => {
    element.addEventListener("click", function() {
      handle.show_gym_dots(this);
    })
  });
}

/**
 * 主函数
 */
(function () {
  var handle = new sim.Exercise_Params();
  watch_btn(handle);
  watch_preset(handle);
  watch_dots(handle);
})();
