"""
This script renames the image slices that come out of Illustrator when using "Save for Web and Devices". The list of
names should map to the badges in the files when reading left to right, top to bottom.
"""
import shutil

names = [
    "adjust-water-heater-temperature-action-badge-0-mega",
    "adjust-water-heater-temperature-action-badge-0-large",
    "adjust-water-heater-temperature-action-badge-0-large-inactive",
    "adjust-water-heater-temperature-action-badge-0-small",
    "adjust-water-heater-temperature-action-badge-0-small-inactive",
    "adjust-water-heater-temperature-action-badge-0-white",
    "trendsetter-badge-0-mega",
    "trendsetter-badge-0-large",
    "trendsetter-badge-0-large-inactive",
    "trendsetter-badge-0-small",
    "trendsetter-badge-0-small-inactive",
    "trendsetter-badge-0-white",
    "social-media-maven-badge-0-mega",
    "social-media-maven-badge-0-large",
    "social-media-maven-badge-0-large-inactive",
    "social-media-maven-badge-0-small",
    "social-media-maven-badge-0-small-inactive",
    "social-media-maven-badge-0-white",
    "social-media-maven-badge-1-mega",
    "social-media-maven-badge-1-large",
    "social-media-maven-badge-1-large-inactive",
    "social-media-maven-badge-1-small",
    "social-media-maven-badge-1-small-inactive",
    "social-media-maven-badge-1-white",
    "social-media-maven-badge-2-mega",
    "social-media-maven-badge-2-large",
    "social-media-maven-badge-2-large-inactive",
    "social-media-maven-badge-2-small",
    "social-media-maven-badge-2-small-inactive",
    "social-media-maven-badge-2-white",
    "follow-through-badge-0-mega",
    "follow-through-badge-0-large",
    "follow-through-badge-0-large-inactive",
    "follow-through-badge-0-small",
    "follow-through-badge-0-small-inactive",
    "follow-through-badge-0-white",
    "follow-through-badge-1-mega",
    "follow-through-badge-1-large",
    "follow-through-badge-1-large-inactive",
    "follow-through-badge-1-small",
    "follow-through-badge-1-small-inactive",
    "follow-through-badge-1-white",
    "follow-through-badge-2-mega",
    "follow-through-badge-2-large",
    "follow-through-badge-2-large-inactive",
    "follow-through-badge-2-small",
    "follow-through-badge-2-small-inactive",
    "follow-through-badge-2-white",
    "follow-through-badge-3-mega",
    "follow-through-badge-3-large",
    "follow-through-badge-3-large-inactive",
    "follow-through-badge-3-small",
    "follow-through-badge-3-small-inactive",
    "follow-through-badge-3-white",
    "momentum-builder-badge-0-mega",
    "momentum-builder-badge-0-large",
    "momentum-builder-badge-0-large-inactive",
    "momentum-builder-badge-0-small",
    "momentum-builder-badge-0-small-inactive",
    "momentum-builder-badge-0-white",
    "dogged-badge-0-mega",
    "dogged-badge-0-large",
    "dogged-badge-0-large-inactive",
    "dogged-badge-0-small",
    "dogged-badge-0-small-inactive",
    "dogged-badge-0-white",
    "dogged-badge-1-mega",
    "dogged-badge-1-large",
    "dogged-badge-1-large-inactive",
    "dogged-badge-1-small",
    "dogged-badge-1-small-inactive",
    "dogged-badge-1-white",
    "dogged-badge-2-mega",
    "dogged-badge-2-large",
    "dogged-badge-2-large-inactive",
    "dogged-badge-2-small",
    "dogged-badge-2-small-inactive",
    "dogged-badge-2-white",
    "dogged-badge-3-mega",
    "dogged-badge-3-large",
    "dogged-badge-3-large-inactive",
    "dogged-badge-3-small",
    "dogged-badge-3-small-inactive",
    "dogged-badge-3-white",
    "founding-father-badge-0-mega",
    "founding-father-badge-0-large",
    "founding-father-badge-0-large-inactive",
    "founding-father-badge-0-small",
    "founding-father-badge-0-small-inactive",
    "founding-father-badge-0-white",
    "gift-of-gab-badge-0-mega",
    "gift-of-gab-badge-0-large",
    "gift-of-gab-badge-0-large-inactive",
    "gift-of-gab-badge-0-small",
    "gift-of-gab-badge-0-small-inactive",
    "gift-of-gab-badge-0-white",
    "gift-of-gab-badge-1-mega",
    "gift-of-gab-badge-1-large",
    "gift-of-gab-badge-1-large-inactive",
    "gift-of-gab-badge-1-small",
    "gift-of-gab-badge-1-small-inactive",
    "gift-of-gab-badge-1-white",
    "gift-of-gab-badge-2-mega",
    "gift-of-gab-badge-2-large",
    "gift-of-gab-badge-2-large-inactive",
    "gift-of-gab-badge-2-small",
    "gift-of-gab-badge-2-small-inactive",
    "gift-of-gab-badge-2-white",
    "gift-of-gab-badge-3-mega",
    "gift-of-gab-badge-3-large",
    "gift-of-gab-badge-3-large-inactive",
    "gift-of-gab-badge-3-small",
    "gift-of-gab-badge-3-small-inactive",
    "gift-of-gab-badge-3-white",
    "hosting-hero-badge-0-mega",
    "hosting-hero-badge-0-large",
    "hosting-hero-badge-0-large-inactive",
    "hosting-hero-badge-0-small",
    "hosting-hero-badge-0-small-inactive",
    "hosting-hero-badge-0-white",
    "unbelievable-badge-0-mega",
    "unbelievable-badge-0-large",
    "unbelievable-badge-0-large-inactive",
    "unbelievable-badge-0-small",
    "unbelievable-badge-0-small-inactive",
    "unbelievable-badge-0-white",
    "shout-out-badge-0-mega",
    "shout-out-badge-0-large",
    "shout-out-badge-0-large-inactive",
    "shout-out-badge-0-small",
    "shout-out-badge-0-small-inactive",
    "shout-out-badge-0-white",
    "storyteller-badge-0-mega",
    "storyteller-badge-0-large",
    "storyteller-badge-0-large-inactive",
    "storyteller-badge-0-small",
    "storyteller-badge-0-small-inactive",
    "storyteller-badge-0-white",
    "paparazzi-badge-0-mega",
    "paparazzi-badge-0-large",
    "paparazzi-badge-0-large-inactive",
    "paparazzi-badge-0-small",
    "paparazzi-badge-0-small-inactive",
    "paparazzi-badge-0-white",
    "save-with-manual-thermostat-action-badge-0-mega",
    "save-with-manual-thermostat-action-badge-0-large",
    "save-with-manual-thermostat-action-badge-0-large-inactive",
    "save-with-manual-thermostat-action-badge-0-small",
    "save-with-manual-thermostat-action-badge-0-small-inactive",
    "save-with-manual-thermostat-action-badge-0-white",
    "retire-second-refrigerator-action-badge-0-mega",
    "retire-second-refrigerator-action-badge-0-large",
    "retire-second-refrigerator-action-badge-0-large-inactive",
    "retire-second-refrigerator-action-badge-0-small",
    "retire-second-refrigerator-action-badge-0-small-inactive",
    "retire-second-refrigerator-action-badge-0-white",
    "set-your-computer-sleep-automatically-action-badge-0-mega",
    "set-your-computer-sleep-automatically-action-badge-0-large",
    "set-your-computer-sleep-automatically-action-badge-0-large-inactive",
    "set-your-computer-sleep-automatically-action-badge-0-small",
    "set-your-computer-sleep-automatically-action-badge-0-small-inactive",
    "set-your-computer-sleep-automatically-action-badge-0-white",
    "replace-your-windows-action-badge-0-mega",
    "replace-your-windows-action-badge-0-large",
    "replace-your-windows-action-badge-0-large-inactive",
    "replace-your-windows-action-badge-0-small",
    "replace-your-windows-action-badge-0-small-inactive",
    "replace-your-windows-action-badge-0-white",
    "insulate-your-windows-action-badge-0-mega",
    "insulate-your-windows-action-badge-0-large",
    "insulate-your-windows-action-badge-0-large-inactive",
    "insulate-your-windows-action-badge-0-small",
    "insulate-your-windows-action-badge-0-small-inactive",
    "insulate-your-windows-action-badge-0-white",
    "programmable-thermostat-action-badge-0-mega",
    "programmable-thermostat-action-badge-0-large",
    "programmable-thermostat-action-badge-0-large-inactive",
    "programmable-thermostat-action-badge-0-small",
    "programmable-thermostat-action-badge-0-small-inactive",
    "programmable-thermostat-action-badge-0-white",
    "install-low-flow-sink-aerator-action-badge-0-mega",
    "install-low-flow-sink-aerator-action-badge-0-large",
    "install-low-flow-sink-aerator-action-badge-0-large-inactive",
    "install-low-flow-sink-aerator-action-badge-0-small",
    "install-low-flow-sink-aerator-action-badge-0-small-inactive",
    "install-low-flow-sink-aerator-action-badge-0-white",
    "install-low-flow-shower-head-action-badge-0-mega",
    "install-low-flow-shower-head-action-badge-0-large",
    "install-low-flow-shower-head-action-badge-0-large-inactive",
    "install-low-flow-shower-head-action-badge-0-small",
    "install-low-flow-shower-head-action-badge-0-small-inactive",
    "install-low-flow-shower-head-action-badge-0-white",
    "sensors-timers-for-lights-action-badge-0-mega",
    "sensors-timers-for-lights-action-badge-0-large",
    "sensors-timers-for-lights-action-badge-0-large-inactive",
    "sensors-timers-for-lights-action-badge-0-small",
    "sensors-timers-for-lights-action-badge-0-small-inactive",
    "sensors-timers-for-lights-action-badge-0-white",
    "use-ceiling-fan-winter-action-badge-0-mega",
    "use-ceiling-fan-winter-action-badge-0-large",
    "use-ceiling-fan-winter-action-badge-0-large-inactive",
    "use-ceiling-fan-winter-action-badge-0-small",
    "use-ceiling-fan-winter-action-badge-0-small-inactive",
    "use-ceiling-fan-winter-action-badge-0-white",
    "use-ceiling-fan-summer-action-badge-0-mega",
    "use-ceiling-fan-summer-action-badge-0-large",
    "use-ceiling-fan-summer-action-badge-0-large-inactive",
    "use-ceiling-fan-summer-action-badge-0-small",
    "use-ceiling-fan-summer-action-badge-0-small-inactive",
    "use-ceiling-fan-summer-action-badge-0-white",
    "install-chimney-draft-guard-action-badge-0-mega",
    "install-chimney-draft-guard-action-badge-0-large",
    "install-chimney-draft-guard-action-badge-0-large-inactive",
    "install-chimney-draft-guard-action-badge-0-small",
    "install-chimney-draft-guard-action-badge-0-small-inactive",
    "install-chimney-draft-guard-action-badge-0-white",
    "insulate-water-heater-action-badge-0-mega",
    "insulate-water-heater-action-badge-0-large",
    "insulate-water-heater-action-badge-0-large-inactive",
    "insulate-water-heater-action-badge-0-small",
    "insulate-water-heater-action-badge-0-small-inactive",
    "insulate-water-heater-action-badge-0-white",
    "caulk-around-your-windows-action-badge-0-mega",
    "caulk-around-your-windows-action-badge-0-large",
    "caulk-around-your-windows-action-badge-0-large-inactive",
    "caulk-around-your-windows-action-badge-0-small",
    "caulk-around-your-windows-action-badge-0-small-inactive",
    "caulk-around-your-windows-action-badge-0-white",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-mega",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-large",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-large-inactive",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-small",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-small-inactive",
    "replace-your-incandescent-light-bulbs-with-cfls-action-badge-0-white",
    "change-air-conditioning-heater-filters-action-badge-0-mega",
    "change-air-conditioning-heater-filters-action-badge-0-large",
    "change-air-conditioning-heater-filters-action-badge-0-large-inactive",
    "change-air-conditioning-heater-filters-action-badge-0-small",
    "change-air-conditioning-heater-filters-action-badge-0-small-inactive",
    "change-air-conditioning-heater-filters-action-badge-0-white",
    "dial-down-thermostat-action-badge-0-mega",
    "dial-down-thermostat-action-badge-0-large",
    "dial-down-thermostat-action-badge-0-large-inactive",
    "dial-down-thermostat-action-badge-0-small",
    "dial-down-thermostat-action-badge-0-small-inactive",
    "dial-down-thermostat-action-badge-0-white",
    "eliminate-standby-vampire-power-action-badge-0-mega",
    "eliminate-standby-vampire-power-action-badge-0-large",
    "eliminate-standby-vampire-power-action-badge-0-large-inactive",
    "eliminate-standby-vampire-power-action-badge-0-small",
    "eliminate-standby-vampire-power-action-badge-0-small-inactive",
    "eliminate-standby-vampire-power-action-badge-0-white",
    "wash-clothes-cold-water-action-badge-0-mega",
    "wash-clothes-cold-water-action-badge-0-large",
    "wash-clothes-cold-water-action-badge-0-large-inactive",
    "wash-clothes-cold-water-action-badge-0-small",
    "wash-clothes-cold-water-action-badge-0-small-inactive",
    "wash-clothes-cold-water-action-badge-0-white",
    "insulate-water-pipes-action-badge-0-mega",
    "insulate-water-pipes-action-badge-0-large",
    "insulate-water-pipes-action-badge-0-large-inactive",
    "insulate-water-pipes-action-badge-0-small",
    "insulate-water-pipes-action-badge-0-small-inactive",
    "insulate-water-pipes-action-badge-0-white",
    "have-home-energy-audit-action-badge-0-mega",
    "have-home-energy-audit-action-badge-0-large",
    "have-home-energy-audit-action-badge-0-large-inactive",
    "have-home-energy-audit-action-badge-0-small",
    "have-home-energy-audit-action-badge-0-small-inactive",
    "have-home-energy-audit-action-badge-0-white",
    "replace-your-outdated-refrigerator-action-badge-0-mega",
    "replace-your-outdated-refrigerator-action-badge-0-large",
    "replace-your-outdated-refrigerator-action-badge-0-large-inactive",
    "replace-your-outdated-refrigerator-action-badge-0-small",
    "replace-your-outdated-refrigerator-action-badge-0-small-inactive",
    "replace-your-outdated-refrigerator-action-badge-0-white",
    "champion-challenger-badge-0-mega",
    "champion-challenger-badge-0-large",
    "champion-challenger-badge-0-large-inactive",
    "champion-challenger-badge-0-small",
    "champion-challenger-badge-0-small-inactive",
    "champion-challenger-badge-0-white",
    "idea-machine-badge-0-mega",
    "idea-machine-badge-0-large",
    "idea-machine-badge-0-large-inactive",
    "idea-machine-badge-0-small",
    "idea-machine-badge-0-small-inactive",
    "idea-machine-badge-0-white",
    "idea-machine-badge-1-mega",
    "idea-machine-badge-1-large",
    "idea-machine-badge-1-large-inactive",
    "idea-machine-badge-1-small",
    "idea-machine-badge-1-small-inactive",
    "idea-machine-badge-1-white",
    "idea-machine-badge-2-mega",
    "idea-machine-badge-2-large",
    "idea-machine-badge-2-large-inactive",
    "idea-machine-badge-2-small",
    "idea-machine-badge-2-small-inactive",
    "idea-machine-badge-2-white",
    "idea-machine-badge-3-mega",
    "idea-machine-badge-3-large",
    "idea-machine-badge-3-large-inactive",
    "idea-machine-badge-3-small",
    "idea-machine-badge-3-small-inactive",
    "idea-machine-badge-3-white"
]

renamed_count = 0
failed_count = 0
list_index = 0
row_count = 0
old_name_count = 1
base_name = "_badges"
path = "../static/images/badges"
for name in names:
    old_name = "%s/%s_%02d.png" % (path, base_name, old_name_count)
    new_name = "%s/%s.png" % (path, names[list_index])
    try:
        shutil.move(old_name, new_name)
        renamed_count += 1
    except Exception, e:
        print "failed to copy %s (%s)" % (old_name, e)
        failed_count += 1

    list_index += 1
    row_count += 1
    old_name_count += 1

    #Add in some extra count to compensate for empty slices that aren't output
    if row_count == 6:
        row_count = 0
        old_name_count += 3

print "============================================"
print "Renamed %d of %d files. (%d failures)" % (renamed_count, len(names), failed_count)
print ""
