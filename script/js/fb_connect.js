/**
 * This is function set that connects backend and frontend
 */

export function get_start_btn() {
    return document.getElementById('start_btn');
}

export function get_reset_btn() {
    return document.getElementById('reset_btn');
}

export function get_all_gym_row() {
    return document.querySelectorAll('.gym_row');
}

export function get_all_attr_select() {
    return document.querySelectorAll('.attr_select');
}

export function get_attr_select(element) {
    return element.querySelector('.attr_select');
}

export function get_preset_select() {
    return document.getElementById('preset_selector');
}

export function get_result_label() {
    return [
      document.getElementById("str_label"),
      document.getElementById("def_label"),
      document.getElementById("spd_label"),
      document.getElementById("dex_label"),
    ];
}

export function get_stats_canvas() {
    return document.getElementById("stats_change_graph");
}

export function get_start_opt(element) {
    return element.querySelector('input[name="start_opt"');
}

export function get_stop_opt(element) {
    return element.querySelector('input[name="stop_opt"');
}

export function get_other_perks() {
  return [
    document.getElementById("faction_perks").value,
    document.getElementById("property_perks").value,
  ];
}

export function get_gym_dots() {
    return document.getElementById("gym_dots");
}

export function get_all_stop_select() {
    return document.querySelectorAll('input[name="stop_opt"');
}