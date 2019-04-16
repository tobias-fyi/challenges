// original filename = pdf_modify.js
// fetches input PDF + loads it into Uint8Array + feeds to pdf-lib

// Set up coordinates for data fields
// TASK_01 : Pull content from ModelField ids
let field_data = {
    order_info: {
        school: {
            data: "El Dorado High",
            pos: [184, 680],
        },
        address: {
            data: "777 Golden Rd",
            pos: [142, 655],
        },
        city: {
            data: "Golden",
            pos: [72, 631],
        },
        state_code: {
            data: "CO",
            pos: [360, 631],
        },
        zip_code: {
            data: "11111",
            pos: [485, 631],
        },
        phone: {
            data: "1112334444",
            pos: [84, 606],
        },
    },
    boxes: {
        qty1: {
            data: "XX",
            pos: [525, 490],
        },
        qty2: {
            data: "XX",
            pos: [525, 461],
        },
        qty3: {
            data: "XX",
            pos: [525, 343],
        },
        qty4: {
            data: "XX",
            pos: [525, 314],
        },
    },
    billing_info: {
        name: {
            data: "Miguel Tulio",
            pos: [84, 208],
        },
        school: {
            data: "El Dorado High",
            pos: [184, 680],
        },
        address: {
            data: "777 Golden Rd",
            pos: [142, 655],
        },
        city: {
            data: "Golden",
            pos: [72, 631],
        },
        state_code: {
            data: "CO",
            pos: [360, 631],
        },
        zip_code: {
            data: "11111",
            pos: [485, 631],
        },
        phone: {
            data: "1112334444",
            pos: [84, 606],
        },
        fax: {
            data: "",
            pos: [360, 106]
        },
        email: {
            data: "",
            pos: [84, 82],
        },
    },
};

let custom_colors = {
    dpurp: [.50, .50, .50],
    gold1: [.86, .47, .07],
    gold2: [.68, .58, .42],
};

// "import" pdf-lib functions
let PDFDocumentFactory = PDFLib.PDFDocumentFactory;
let PDFDocumentWriter = PDFLib.PDFDocumentWriter;
let PDFStandardFonts = PDFLib.StandardFonts;
let drawText = PDFLib.drawText;

// Create the request
let pdfStaticURL = '/static/orderform/formeasure01.pdf';
let pdfInit = {
    headers: { "Content-Type": "application/pdf" },
};
let pdfRequest = new Request(pdfStaticURL, pdfInit);

// Process the Uint8Array once resolved from fetch / promise
function processArray(typedArray) {
    // Load the PDF file (Uint8Array) into a PDFDocument object
    const pdfDoc = PDFDocumentFactory.load(typedArray);

    // Set font
    const [helveticaRef, helveticaFont] = pdfDoc.embedStandardFont(
        PDFStandardFonts.Helvetica,
    );

    const pages = pdfDoc.getPages();
    const page = pages[0];

    page.addFontDictionary('Helvetica', helveticaRef);

    const contentStream = pdfDoc.createContentStream(
        drawText(helveticaFont.encodeText(field_data.order_info.school.data), {
            x: field_data.order_info.school.pos[0],
            y: field_data.order_info.school.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold1,
        }),
        drawText(helveticaFont.encodeText(field_data.order_info.address.data), {
            x: field_data.order_info.address.pos[0],
            y: field_data.order_info.address.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.order_info.city.data), {
            x: field_data.order_info.city.pos[0],
            y: field_data.order_info.city.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.order_info.state_code.data), {
            x: field_data.order_info.state_code.pos[0],
            y: field_data.order_info.state_code.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold1,
        }),
        drawText(helveticaFont.encodeText(field_data.order_info.zip_code.data), {
            x: field_data.order_info.zip_code.pos[0],
            y: field_data.order_info.zip_code.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.order_info.phone.data), {
            x: field_data.order_info.phone.pos[0],
            y: field_data.order_info.phone.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.boxes.qty1.data), {
            x: field_data.boxes.qty1.pos[0],
            y: field_data.boxes.qty1.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.boxes.qty2.data), {
            x: field_data.boxes.qty2.pos[0],
            y: field_data.boxes.qty2.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.boxes.qty3.data), {
            x: field_data.boxes.qty3.pos[0],
            y: field_data.boxes.qty3.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.boxes.qty4.data), {
            x: field_data.boxes.qty4.pos[0],
            y: field_data.boxes.qty4.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.name.data), {
            x: field_data.billing_info.name.pos[0],
            y: field_data.billing_info.name.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.school.data), {
            x: field_data.billing_info.school.pos[0],
            y: field_data.billing_info.school.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.address.data), {
            x: field_data.billing_info.address.pos[0],
            y: field_data.billing_info.address.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.city.data), {
            x: field_data.billing_info.city.pos[0],
            y: field_data.billing_info.city.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.state_code.data), {
            x: field_data.billing_info.state_code.pos[0],
            y: field_data.billing_info.state_code.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold1,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.zip_code.data), {
            x: field_data.billing_info.zip_code.pos[0],
            y: field_data.billing_info.zip_code.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.gold2,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.phone.data), {
            x: field_data.billing_info.phone.pos[0],
            y: field_data.billing_info.phone.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.fax.data), {
            x: field_data.billing_info.fax.pos[0],
            y: field_data.billing_info.fax.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
        drawText(helveticaFont.encodeText(field_data.billing_info.email.data), {
            x: field_data.billing_info.email.pos[0],
            y: field_data.billing_info.email.pos[1],
            size: 12,
            font: 'Helvetica',
            colorRgb: custom_colors.dpurp,
        }),
    );

    page.addContentStreams(pdfDoc.register(contentStream));

    const pdfBytes = PDFDocumentWriter.saveToBytes(pdfDoc);

    const pdfFileData = new Blob([pdfBytes], { type: "application/pdf" })

    const pdfURL = window.URL.createObjectURL(pdfFileData);

    document.getElementById("download_link").href = pdfURL;
}

// Use fetch() to load the pdf into buffer then to Uint8Array.
fetch(pdfRequest)
    .then(response => response.arrayBuffer())
    .then(arrayBuffer => new Uint8Array(arrayBuffer))
    .then(Uint8Array => processArray(Uint8Array))
    .catch(err => console.log(err));
