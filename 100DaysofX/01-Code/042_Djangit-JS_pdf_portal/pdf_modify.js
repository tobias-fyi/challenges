// original filename = pdf_modify.js
// fetches input PDF + loads it into Uint8Array + feeds to pdf-lib

// Set up coordinates for data fields
let field_coordinates = {
    order_info: {
        school: [184, 680],
        address: [142, 655],
        city: [72, 631],
        state_code: [360, 631],
        zip_code: [485, 631],
        phone: [84, 606],
    },
    boxes: {
        qty1: [525, 490],
        qty2: [525, 461],
        qty3: [525, 343],
        qty4: [525, 314],
    },
    billing_info: {
        name: [84, 208],
        school: [130, 184],
        address: [98, 158],
        city: [72, 132],
        state_code: [360, 132],
        zip_code: [485, 132],
        phone: [84, 106],
        fax: [360, 106],
        email: [84, 82],
    },
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
        drawText(helveticaFont.encodeText('Here is a field with data from my django form'), {
            x: field_coordinates.order_info.school[0],
            y: field_coordinates.order_info.school[1],
            size: 24,
            font: 'Helvetica',
            colorRgb: [0.95, 0.26, 0.21],
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
