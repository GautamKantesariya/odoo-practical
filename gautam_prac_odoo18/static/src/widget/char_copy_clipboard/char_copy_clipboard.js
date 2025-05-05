/** @odoo-module */

import { Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { omit } from "@web/core/utils/objects";
import { CharField } from "@web/views/fields/char/char_field";
import { CopyButton } from "@web/core/copy_button/copy_button";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

class CharCopyClipboard extends Component {
    static components = {
        BaseChar: CharField,
        Copier: CopyButton,
    };

    static props = {
        ...standardFieldProps,
        label: { type: String, optional: true },
    };

    static template = "gautam_prac_odoo18.CharCopyClipboard";

    get charProps() {
        return omit(this.props, "label");
    }

    get textToCopy() {
        return this.props.record.data[this.props.name] || "";
    }
}

export const copyableCharField = {
    component: CharCopyClipboard,
    displayName: _t("Char with Clipboard"),
    supportedTypes: ["char"],
    extractProps: ({ attrs }) => ({
        label: attrs.label,
    }),
};

registry.category("fields").add("copyable_char", copyableCharField);
