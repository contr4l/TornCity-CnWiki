import * as sim from "./simulator_class.js"

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
  var startButton = document.getElementById('start_btn');
  startButton.addEventListener('click', function () {
    console.log("Start Simulation!");
    simulation_process(handle);
  });

  var resetButton = document.getElementById('reset_btn');
  resetButton.addEventListener('click', function () {
    console.log("Reset Simulation Params!");
    handle.reset_all_params();
    document.querySelectorAll('.gym_row').forEach( element => {
      if (element.querySelector('.attr_select').length > 5)
        element.querySelector('.attr_select').selectedIndex = 5;
      else
        element.querySelector('.attr_select').selectedIndex = 0;
    });
  });
}

/** 
 * @param {sim.Exercise_Params} handle 
 */
function watch_preset(handle) {
  var presetOpt = document.getElementById('preset_selector');

  presetOpt.onchange = function () {
    handle.get_start_stop_gym();
    handle.get_initial_stats();
    if (this.selectedIndex == sim.PRESET_SELECTOR_USER_DEFINED) {
      return;
    }
    else {
      document.querySelectorAll('.gym_row').forEach( element => {
        element.querySelector('.attr_select').selectedIndex = 4;
      });
    }
  };
}

/**
 * @param {sim.Exercise_Params} handle
 */
function watch_dots(handle) {
  document.querySelectorAll(".attr_select").forEach(element => {
    element.addEventListener("click", function() {
      handle.show_gym_dots(this);
    })
  });
}

(function () {
  var handle = new sim.Exercise_Params();
  watch_btn(handle);
  watch_preset(handle);
  watch_dots(handle);
})();
