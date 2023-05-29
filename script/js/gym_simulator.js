import * as sim from "./simulator_class.js"


function simulation_process(handle) {
  handle.reset_all_params();

  handle.read_preset();
  handle.read_params();

  handle.initialize();
  handle.show_basic_info();
  handle.iter_process();
  handle.render_result();
}

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
  });
}

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

(function () {
  var handle = new sim.Exercise_Params();
  watch_btn(handle);
  watch_preset(handle);
})();
