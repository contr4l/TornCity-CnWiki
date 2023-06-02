import * as cal_func from "./calculator.js";
import * as cnct from "./fb_connect.js"

function format_num(num) {
  if (num > 1e9) {
    return (num / 1e9).toFixed(2) + 'b';
  }
  else if (num > 1e6) {
    return (num / 1e6).toFixed(2) + 'm';
  }
  else if (num > 1e3) {
    return (num / 1e3).toFixed(2) + 'k';
  }
  else {
    return num.toFixed(2);
  }
}

export class Exercise_Params {
  constructor() {
    console.log("Initializing Exercise_Params");
    this.reset_all_params();
    this.show_basic_info();
  }

  reset_all_params() {
    console.log("Resetting all params");
    this.initial_happiness = 5025;
    this.current_happiness = 5025;

    this.current_bonus = 1.0;

    this.start_gym_name = "Premier Fitness";
    // this.stop_gym_name = "Premier Fitness";
    this.stop_gym_name = "George's";
    this.current_gym_name = "Premier Fitness";

    this.current_focus = "def";

    this.current_gym_progress = 0;
    this.current_gym_limit = 0;

    this.current_stats = [0, 0, 0, 0];
    this.stats_progress = [this.current_stats];
    this.exercise_chain = new Array([]);
    this.exercise_idx = 0;

    this.update_callback = null;
  }

  show_basic_info() {
    console.log(`start gym is ${this.start_gym_name}\
                   \nstop  gym is ${this.stop_gym_name} \
                   \ncurrent todo  is ${this.current_focus}\
                   \ncurrent perks is ${this.current_bonus}`);
    console.log(`current stats is \
      \nstr = ${this.current_stats[0].toFixed(2)}, \
      \ndef = ${this.current_stats[1].toFixed(2)}, \
      \nspd = ${this.current_stats[2].toFixed(2)}, \
      \ndex = ${this.current_stats[3].toFixed(2)}`);
  }

  stats_info() {
    return (
      this.current_stats[0].toFixed(2) +
      "," +
      this.current_stats[1].toFixed(2) +
      "," +
      this.current_stats[2].toFixed(2) +
      "," +
      this.current_stats[3].toFixed(2)
    );
  }
}

Exercise_Params.prototype.push_attr = function (stats_name) {
  this.exercise_chain.push(stats_name);
};

Exercise_Params.prototype.clear_attr = function () {
  this.exercise_chain = new Array();
};

Exercise_Params.prototype.last_attr = function () {
  if (this.exercise_chain.length === 0)
    return "str";

  return this.exercise_chain[this.exercise_chain.length - 1]
};

Exercise_Params.prototype.validation_range = function () {
  start_idx = cal_func.find_gym_idx(this.start_gym_name);
  stop_idx = cal_func.find_gym_idx(this.stop_gym_name);

  return stop_idx - start_idx + 1 == this.exercise_chain.length;
};

Exercise_Params.prototype.set_happiness = function (h) {
  this.initial_happiness = h;
};

Exercise_Params.prototype.should_stop_iter = function () {
  // console.log(`current gym is ${this.current_gym_name}\
  //            \ntarget gym is ${this.stop_gym_name}`);
  // console.log(`current progress is ${this.current_gym_progress}, target progress is ${this.current_gym_limit}`);
  return (
    this.current_gym_name == this.stop_gym_name &&
    this.current_gym_progress >= this.final_gym_target
  );
};

Exercise_Params.prototype.initialize = function () {
  this.current_gym_name = this.start_gym_name;
  this.current_happiness = this.initial_happiness;
  this.current_focus = this.exercise_chain[0];

  let gym_idx = cal_func.find_gym_idx(this.current_gym_name);
  this.current_gym_limit = cal_func.gym_exp[gym_idx];
};

Exercise_Params.prototype.update = function (gym_idx) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = this.exercise_chain[gym_idx];
};

Exercise_Params.prototype.overall_greedy_update = function (
  gym_idx) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = cal_func.find_greedy_stats(
    gym_idx,
    this.current_stats,
    false
  );
  this.push_attr(this.current_focus);
};

Exercise_Params.prototype.strspd_greedy_update = function (
  gym_idx) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = cal_func.find_greedy_stats(
    gym_idx,
    this.current_stats,
    true
  );
  this.push_attr(this.current_focus);
};

Exercise_Params.prototype.finish_train = function (gym_idx) {
  this.current_gym_progress = cal_func.gym_exp[gym_idx];
  this.current_gym_limit = cal_func.gym_exp[gym_idx];
  this.stats_progress.push(this.current_stats.slice());
};

Exercise_Params.prototype.get_gym_exp = function (gym_idx) {
  let gym_exp = cal_func.gym_exp[gym_idx];

  if (cal_func.find_gym_idx(this.stop_gym_name) == gym_idx){
    gym_exp = this.final_gym_target;
  }
  if (cal_func.find_gym_idx(this.start_gym_name) == gym_idx){
    gym_exp -= this.current_gym_progress;
  }
  console.log(gym_exp);
  return gym_exp;
}
// process_1: using the same happiness for the whole time
Exercise_Params.prototype.iter_process = function () {
  let start_idx = cal_func.find_gym_idx(this.start_gym_name);
  let stop_idx = cal_func.find_gym_idx(this.stop_gym_name);
  let gym_idx = start_idx;

  while (!this.should_stop_iter()) {
    // Each iteration will finish one gym
    this.update_callback(gym_idx);
    
    let gym_exp = this.get_gym_exp(gym_idx);

    let train_times = cal_func.get_total_train_times(gym_idx, gym_exp);
    let stats_idx = cal_func.stats_idx_map[this.current_focus];

    // console.log(`train_times: ${train_times}`);
    for (let i = 0; i < train_times; i++) {
      this.current_stats[stats_idx] += cal_func.single_train_gains(
        this.current_focus,
        this.current_gym_name,
        this.current_stats[stats_idx],
        this.current_happiness,
        this.current_bonus
      );
    }
    // console.log(this.current_focus, this.current_gym_name, this.current_stats[stats_idx].toFixed(2), this.current_happiness, this.current_bonus);

    // console.log(
    //   `finish ${this.current_gym_name}, stats changed to ${this.stats_info()}`
    // );
    // hit the stop condition
    this.finish_train(gym_idx);
    gym_idx += 1;
  }
  console.log("train order is ", this.exercise_chain.slice(start_idx, stop_idx+1));
};

function pathTo(ctx, xStart, yStart, xStep, yStep, x, y, move=true) {
  if (move)
    ctx.moveTo(xStart + x*xStep, yStart - y*yStep);
  else
    ctx.lineTo(xStart + x*xStep, yStart - y*yStep);
}

function drawLine(ctx, xStart, yStart, xStep, yStep, x1, y1, x2, y2, color) {
  ctx.strokeStyle = color;
  ctx.beginPath();
  pathTo(ctx, xStart, yStart, xStep, yStep, x1, y1);
  pathTo(ctx, xStart, yStart, xStep, yStep, x2, y2, false);
  ctx.stroke();
}

function resize_canvas(canvas, ctx) {
  let dpr = window.devicePixelRatio; // 假设dpr为2
  let { width: cssWidth, height: cssHeight } = canvas.getBoundingClientRect();
  canvas.width = dpr * cssWidth;
  canvas.height = dpr * cssHeight;
  // ctx.scale(dpr,dpr);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawAxis(canvas, ctx, xMin, xMax, yMin, yMax, coef){
  const xMargin = Math.floor(canvas.width * coef);
  const yMargin = Math.floor(canvas.height * coef);
  const xStep = (canvas.width - 2 * xMargin) / (xMax - xMin);
  const yStep = (canvas.height - 2 * yMargin) / (yMax - yMin);
  const xStart = xMargin;
  const yStart = canvas.height - yMargin;
  ctx.strokeStyle = "black";
  ctx.beginPath();
  ctx.moveTo(xMargin, yMargin);
  ctx.lineTo(xMargin, canvas.height - yMargin);
  ctx.lineTo(canvas.width - xMargin, canvas.height - yMargin);
  ctx.lineWidth = 6;
  ctx.stroke();
  return [xStep, yStep, xStart, yStart];
}

export var PRESET_SELECTOR_USER_DEFINED = 0;
export var PRESET_SELECTOR_GREEDY_OVERALL = 1;
export var PRESET_SELECTOR_GREEDY_STR_SPD = 2;
Exercise_Params.prototype.read_preset = function () {
  let element = cnct.get_preset_select();

  if (element.selectedIndex == PRESET_SELECTOR_USER_DEFINED) {
    this.update_callback = this.update;
    return false;
  } else if (element.selectedIndex == PRESET_SELECTOR_GREEDY_OVERALL) {
    console.log("PRESET_SELECTOR_GREEDY_OVERALL is selected");
    this.update_callback = this.overall_greedy_update;
  } else if (element.selectedIndex == PRESET_SELECTOR_GREEDY_STR_SPD) {
    console.log("PRESET_SELECTOR_GREEDY_STR_SPD is selected");
    this.update_callback = this.strspd_greedy_update;
  }
  return true;
};

Exercise_Params.prototype.get_exercise_chain = function () {
  this.clear_attr();
  var alert_ = false;
  cnct.get_all_attr_select().forEach((element) => {
    let idx = element.selectedIndex;
    if (element.options[idx].text == "same as above") {
      this.push_attr(this.last_attr());
    } else if (element.options[idx].text == "PRESET" && !alert_) {
      alert_ = true;
      alert("PRESET not compatible with User Defined, the result would be incorrect");
      return;
    }
    else {
      this.push_attr(element.options[idx].text);
    }
  });
  // console.log(this.exercise_chain);
};

Exercise_Params.prototype.get_start_stop_gym = function () {
  cnct.get_all_gym_row().forEach((element) => {
    // console.log("check", element.querySelector('td').textContent);
    if (cnct.get_start_opt(element).checked) {
      this.start_gym_name = element.querySelector("td").textContent;
    }
    if (cnct.get_stop_opt(element).checked) {
      this.stop_gym_name = element.querySelector("td").textContent;
    }
  });

  this.current_gym_progress = Number(document.getElementById("initial_progress").value);
  this.final_gym_target = Number(document.getElementById("final_progress").value);

  console.log("start from", this.start_gym_name, "end at", this.stop_gym_name, "final progress", this.final_gym_target);
};

Exercise_Params.prototype.get_initial_stats = function () {
  this.current_stats[0] = Number(document.getElementById('str_input').value);
  this.current_stats[1] = Number(document.getElementById('def_input').value);
  this.current_stats[2] = Number(document.getElementById('spd_input').value);
  this.current_stats[3] = Number(document.getElementById('dex_input').value);
  this.stats_progress = [this.current_stats.slice()];
};

Exercise_Params.prototype.get_happiness = function () {
  this.initial_happiness = Number(document.getElementById('happiness_input').value);
};

function parse_perks(percentage) {
  if (isNaN(percentage) || Number(faction_perks) == 0) {
    return 1;
  }
  return 1 + Number(percentage / 100);
}

Exercise_Params.prototype.get_other_perks = function () {
  let [faction_perks, property_perks] = cnct.get_other_perks();
  console.log("faction_perks = " + faction_perks, "property_perks = " + property_perks);

  this.current_bonus *= parse_perks(faction_perks);
  this.current_bonus *= parse_perks(property_perks);
};

Exercise_Params.prototype.read_params = function () {
  // when "start" button is clicked, read all params set from webpage
  // and start simulation

  // Step 1: get exercise chain
  if (!this.read_preset()) {
    this.get_exercise_chain();
  }

  // Step 2: get start and stop gym name
  this.get_start_stop_gym();

  // Step 3: get happiness
  this.get_happiness();

  // Step 4: get initial stats
  this.get_initial_stats();


  // Step 5: get bonus perks
  this.get_other_perks();
};

/**
 *
 * @param {NamedNodeMap} dom
 */
Exercise_Params.prototype.show_gym_dots = function (dom) {
  let gym_name = dom.parentNode.previousElementSibling.textContent;
  let gym_dots = cal_func.find_gym_dot(gym_name);
  console.log("gym is ", gym_name, "dots is ", gym_dots);

  let canvas = cnct.get_gym_dots();
  var ctx = canvas.getContext("2d");
  resize_canvas(canvas, ctx);


  // draw axis
  const xMin = 0, xMax = 5;
  const yMin = 0, yMax = Math.max(...gym_dots.filter(x => !isNaN(x)));
  let [xStep, yStep, xStart, yStart] = drawAxis(canvas, ctx, xMin, xMax, yMin, yMax, 0.1);

  ctx.font = "20px Arial Bold";
  ctx.fillStyle = "black";
  ctx.fillText(gym_name, canvas.width / 2 - 7.5 * gym_name.length, yStep * 0.7);

  let color = ["red", "green", "yellow", "purple"];
  let text = ["str", "def", "spd", "dex"];
  for (let i = cal_func.STR; i <= cal_func.DEX; i ++)
  {
    if (!isNaN(gym_dots[i])){
      ctx.fillStyle = color[i];
      ctx.fillRect(xStart + (i + 0.5) * xStep, yStart - 0.1 * yStep, 0.6 * xStep, -gym_dots[i] * yStep * 0.8);
    }
    ctx.fillStyle = "black";
    ctx.fillText(text[i], xStart + (i + 0.75) * xStep, yStart + 24);
    ctx.fillText(gym_dots[i].toFixed(1), xStart + (i + 0.75) * xStep, yStart -gym_dots[i] * yStep * 0.85);
  }
}

Exercise_Params.prototype.render_result = function () {
  let self = this;
  (function fill_result_table() {
    let [str_result, def_result, spd_result, dex_result] = cnct.get_result_label();
    str_result.textContent = format_num(self.current_stats[0]);
    def_result.textContent = format_num(self.current_stats[1]);
    spd_result.textContent = format_num(self.current_stats[2]);
    dex_result.textContent = format_num(self.current_stats[3]);
  })();

  (function render_canvas() {
    let canvas = cnct.get_stats_canvas()
    let ctx = canvas.getContext("2d");
    resize_canvas(canvas,ctx);

    let start_idx = cal_func.find_gym_idx(self.start_gym_name);
    let stop_idx = cal_func.find_gym_idx(self.stop_gym_name);
    
    // draw axis
    const yMargin = Math.floor(canvas.height * 0.075);
    const xMin = 0, xMax = stop_idx - start_idx + 1;
    const yMin = 0, yMax = Math.max(...self.current_stats);
    let [xStep, yStep, xStart, yStart] = drawAxis(canvas, ctx, xMin, xMax, yMin, yMax, 0.075);

    ctx.lineWidth = 3;
    for (let i = xMin; i <= xMax; i++) {
      drawLine(ctx, xStart, yStart, xStep, yStep, i-xMin, 0, i-xMin, yMax / 50, "black");
      drawLine(ctx, xStart, yStart, xStep, yStep, 0, yMax / (xMax - xMin + 1) * (i - xMin), xMax / 90, yMax / (xMax - xMin + 1) * (i - xMin), "black");
    }

    // draw four lines
    let x = new Array();
    let y = new Array();
    for (let i = start_idx; i <= stop_idx + 1; i++) {
      x.push(i - start_idx);
      y.push(self.stats_progress[i - start_idx].slice());
    }

    let color = ["red", "green", "yellow", "purple"];
    for (let i = cal_func.STR; i <= cal_func.DEX; i++){
      ctx.strokeStyle = color[i];
      ctx.beginPath();
      pathTo(ctx, xStart, yStart, xStep, yStep, x[0], y[0][i]);
      for (let j = 1; j < x.length; j++) {
        pathTo(ctx, xStart, yStart, xStep, yStep, x[j], y[j][i], false);
      }
      ctx.lineWidth = 3;
      ctx.stroke();
      ctx.save();
    }

    // draw legend
    const legend_fontsize = 24;
    let x_offset = 100;
    let legend_y_start = yMargin * 2;
    ctx.font = legend_fontsize+"px Mono";

    ctx.fillStyle = "red";
    ctx.fillText("Str", x_offset, legend_y_start);
    ctx.fillRect(x_offset + legend_fontsize * 3, legend_y_start - legend_fontsize / 2, legend_fontsize * 4, yMargin / 5);
    
    ctx.fillStyle = "green";
    legend_y_start += yMargin;
    ctx.fillText("Def", x_offset, legend_y_start);
    ctx.fillRect(x_offset + legend_fontsize * 3, legend_y_start - legend_fontsize / 2, legend_fontsize * 4, yMargin / 5);

    ctx.fillStyle = "yellow";
    legend_y_start += yMargin;
    ctx.fillText("Spd", x_offset, legend_y_start);
    ctx.fillRect(x_offset + legend_fontsize * 3, legend_y_start - legend_fontsize / 2, legend_fontsize * 4, yMargin / 5);
    
    ctx.fillStyle = "purple";
    legend_y_start += yMargin;
    ctx.fillText("Dex", x_offset, legend_y_start);
    ctx.fillRect(x_offset + legend_fontsize * 3, legend_y_start - legend_fontsize / 2, legend_fontsize * 4, yMargin / 5);
    
    // ctx.strokeStyle = "black";
    // ctx.lineWidth = 3;
    // ctx.strokeRect(canvas.width / 2 - 32, 2*yMargin - 40, 320, legend_y_start - yMargin);

})();
};

export function Refresh_Target(dom)
{
    let gym_name = dom.parentNode.parentNode.querySelector("td").textContent;
    let gym_idx = cal_func.find_gym_idx(gym_name);
    document.getElementById("final_progress").value = cal_func.gym_exp[gym_idx];
}